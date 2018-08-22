from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'0$', show_0, name="show_0"),
]
