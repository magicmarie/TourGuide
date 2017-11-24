"This will have all the url routes for the web app"

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^tourist_home/$', views.tourist_home, name='tourist_home'),
    # url(r'^login/$', views.login, name='login'),
]