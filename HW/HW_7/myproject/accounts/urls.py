from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),    # (1점)
    path('logout/', views.logout_view, name='logout'),  # (1점)
    path('home/', views.home_view, name='home'),        # (1점)
]
