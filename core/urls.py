
from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('user/', views.UserAPIView.as_view(), name='user'),
]