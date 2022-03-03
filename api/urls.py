"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from cases.views import AppointmentViewSet, ApprovalViewSet, BiddingViewSet, CaseViewSet, CommentViewSet, ContractingViewSet, DomainViewSet, PlanningViewSet, TeamViewSet, UserDetailsViewSet, UserViewSet
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
# app data
# router.register(r'appointments', AppointmentViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'domains', DomainViewSet)
# router.register(r'teams', TeamViewSet)
# router.register(r'userdetails', UserDetailsViewSet)
# router.register(r'plannings', PlanningViewSet)
# router.register(r'biddings', BiddingViewSet)
# router.register(r'approvals', ApprovalViewSet)
# router.register(r'contractings', ContractingViewSet)
# router.register(r'cases', CaseViewSet)
# router.register(r'comments', CommentViewSet)
# authentication
# router.register(r'token', jwt_views.TokenObtainPairView.as_view())
# router.register(r'token/refresh', jwt_views.TokenRefreshView.as_view())

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/', include('cases.url')),
    path('admin/', admin.site.urls),
]
