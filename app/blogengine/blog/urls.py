from django.urls import path


from .views import *
from django.urls import include


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slag>/', post_detail, name='post_detail_url')
    ]