from django.urls import path, include
from rest_framework import routers
from .views import AppointmentViewSet, ApprovalViewSet, BiddingViewSet, CaseViewSet, CommentViewSet, ContractingViewSet, DomainViewSet, PlanningViewSet, TeamViewSet, UserDetailsViewSet, UserViewSet

router = routers.DefaultRouter()
# app data
router.register(r'appointments', AppointmentViewSet)
router.register(r'users', UserViewSet)
router.register(r'domains', DomainViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'userdetails', UserDetailsViewSet)
router.register(r'plannings', PlanningViewSet)
router.register(r'biddings', BiddingViewSet)
router.register(r'approvals', ApprovalViewSet)
router.register(r'contractings', ContractingViewSet)
router.register(r'cases', CaseViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]