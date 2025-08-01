from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterViewSet.as_view(), name='register'),
    path('login/', views.LoginViewSet.as_view(), name='login'),
]
