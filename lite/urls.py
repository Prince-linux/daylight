from django.conf.urls import include, url
from .views import index

urlpatterns = [
    url('', index, name="index")
]