from django.urls import path
from .views import receive_post

urlpatterns = [
    path('post/', receive_post),
]
