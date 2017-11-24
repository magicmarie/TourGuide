from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^tourapp/', include('tourapp.urls', namespace='tourapi', app_name='tourapi')),
    url(r'^admin/', admin.site.urls),
]
