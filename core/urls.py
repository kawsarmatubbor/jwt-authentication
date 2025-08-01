from django.urls import path
from . import views

urlpatterns = [
    path('protected/', views.ProtectedViewSet.as_view(), name='protected'),
]
