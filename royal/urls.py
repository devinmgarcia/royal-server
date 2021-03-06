from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from royalapi.models import *
from royalapi.views import *
from django.urls import path
from django.contrib import admin

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'products', ProductsView, 'product')
router.register(r'product_types', ProductTypesView, 'product_type')
router.register(r'product_images', ProductImageView, 'product_image')
router.register(r'cart', CartView, 'carts')
router.register(r'orders', OrderView, 'order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    url(r'^api-token-auth$', obtain_auth_token),
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
