from django.conf.urls import url, include

from .views import signup

urlpatterns = [
    url(r'^users/register/$', signup),
    url(r'^users/', include("django.contrib.auth.urls"))

]
