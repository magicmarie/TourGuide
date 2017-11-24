from django.conf.urls import url
from tourapi import views

urlpatterns = [
	url(r'tourists/register/', views.api_register_tourist, name='api_register_tourist'),
    url(r'tourists/all/', views.api_get_tourists, name='api_tourists'),
    url(r'tourists/(?P<tourist>\d+)/', views.api_get_single_tourist, name='api_single_tourist'),
]
