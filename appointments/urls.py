from django.urls import path
from .views import *
app_name = "appointments"
urlpatterns = [
    path('', home , name="Home"),
    path('about/', about , name="About"),
    path('gallery/', gallery , name="Gallery"),
    path('contact/', contact , name="Contact"),
]