from royalapi.models.customer import Customer
from royalapi.models.cart import Cart
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from royalapi.models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for products"""
    class Meta:
        model = Order
        fields = ('id','recipient', 'cart', 'billing_street_one', 'billing_street_two', 'billing_city', 'billing_state', 'billing_zip', 'shipping_street_one', 'shipping_street_two', 'shipping_city', 'shipping_state', 'shipping_zip', 'tracking_info', 'date')
        depth = 3

class OrderView(ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(
            orders, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        # find the cart for this order
        cart = Cart.objects.get(pk=request.data['cart_id'])
        try:
            # save the new order
            order = Order.objects.create(
                cart = cart,
                recipient = request.data['purchase_units'][0]['shipping']['name']['full_name'],
                billing_street_one = request.data['purchase_units'][0]['shipping']['address']['address_line_1'],
                billing_city = request.data['purchase_units'][0]['shipping']['address']['admin_area_2'],
                billing_state = request.data['purchase_units'][0]['shipping']['address']['admin_area_1'],
                billing_zip = request.data['purchase_units'][0]['shipping']['address']['postal_code']
            )  
            # send email confirmation
            subject = f'Thanks for your order, {order.recipient}!'
            html_message = render_to_string('mail_template.html', {'order': order})
            plain_message = strip_tags(html_message)
            from_email = 'devinmgarcia@gmail.com'
            to = 'dmg1021@gmail.com'

            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

            # html_message = render_to_string('mail_template.html', {'context': order})
            # mail.send_mail(
            #     f'Thanks for your order, {order.recipient}!',
            #     strip_tags(html_message),
            #     settings.EMAIL_HOST_USER,
            #     ['dmg1021@gmail.com'],
            #     html_message=html_message,
            #     fail_silently=False,
            # )

            # close the cart
            cart.order_complete = True
            cart.save()
            # create a new cart for the customer
            customer = Customer.objects.get(user=request.auth.user)
            Cart.objects.create(
                customer = customer,
                order_complete = False
            )
            return Response({}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': ex.args[0]})

    def update(self, request, pk=None):

        try:
            order = Order.objects.get(pk=pk)
            order.tracking_info = request.data['tracking_info']
            order.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response({'message': ex.args[0]})

        



