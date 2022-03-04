from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('', CustomTokenObtainPairView.as_view()),
    path('refresh/', jwt_views.TokenRefreshView.as_view())
]