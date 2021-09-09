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
router.register(r'products', Products, 'product')

urlpatterns = [
    url(r'^', include(router.urls)),
]
