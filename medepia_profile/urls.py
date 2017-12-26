from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    #TODO add profile details endpoint
    url(r'^create/$', ProfileCreateView.as_view(), name='create'),



]