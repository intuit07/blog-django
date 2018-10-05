from django.urls import path


from .views import *
from django.urls import include


urlpatterns = [
    path('', posts_list),
    ]