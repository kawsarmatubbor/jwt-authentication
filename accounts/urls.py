from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterViewSet.as_view(), name='register'),
]
