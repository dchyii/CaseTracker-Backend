from urllib import request
from django.http import QueryDict
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Appointment, Domain, Team, UserDetails, Planning, Bidding, Approval, Contracting, Case, Comment
from .serializers import AppointmentSerializer, ApprovalSerializer, BiddingSerializer, CaseSerializer, CommentSerializer, ContractingSerializer, DashboardSerializer, DomainSerializer, PlanningSerializer, TeamSerializer, UserDetailsSerializer, UserSerializer

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlanningViewSet(viewsets.ModelViewSet):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer
    permission_classes = [permissions.IsAuthenticated]

class BiddingViewSet(viewsets.ModelViewSet):
    queryset = Bidding.objects.all()
    serializer_class = BiddingSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContractingViewSet(viewsets.ModelViewSet):
    queryset = Contracting.objects.all()
    serializer_class = ContractingSerializer
    permission_classes = [permissions.IsAuthenticated]

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [permissions.AllowAny]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class DashboardCasesView(ListCreateAPIView):
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return Case.objects.filter(current_step_user=self.request.user)
        return Case.objects.filter(Q(current_step_user=self.request.user) | Q(staffer=self.request.user))

    # def perform_create(self, serializer):
    #     serializer.save(staffer=self.request.user)
    def create(self, request, *args, **kwargs):
        case_data = request.data

        new_case = Case.objects.create(title=case_data["title"], value=case_data["value"], folder_link=case_data["folder_link"], staffer = User.objects.get(id=case_data["staffer"]), current_status = case_data["current_status"], current_step = case_data["current_step"], current_step_user=User.objects.get(id=case_data["current_step_user"]), next_step=case_data["next_step"], next_step_user=User.objects.get(id=case_data["next_step_user"]), planning=Planning.objects.get(id=case_data["planning"]),bidding=Bidding.objects.get(id=case_data["bidding"]), approval=Approval.objects.get(id=case_data["approval"]), contracting=Contracting.objects.get(id=case_data["contracting"]))

        new_case.save()

        serializer = CaseSerializer(new_case)

        return Response(serializer.data)

class DashboardCasesDetailedView(RetrieveUpdateDestroyAPIView):
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field="id"

    def get_queryset(self):
        return Case.objects.filter(current_step_user=self.request.user)




# class DashboardViewSet(viewsets.ModelViewSet):
#     queryset = Case.objects.all()
#     serializer_class = CaseSerializer
#     # lookup_field = 'staffer'

#     @action(detail=True, methods=["get"])
#     def get_cases(self, request, pk=None):
#         user = self.get_object()
#         print("user: " + str(user))
#         current_user_cases = Case.objects.filter('planning' == None)
#         return Response(current_user_cases)

    # def list(self, request):
    #     print("request " + str(request))
    #     current_user = self.request.user
    #     print("user " + str(current_user))
    #     current_user_cases = Case.objects.filter(staffer = current_user)
    #     serializer = CaseSerializer(current_user_cases, many=True)
    #     return Response(serializer.data)

    # def get_queryset(self):
    #     user = self.request.user
    #     print(user)
    #     return []

    # queryset = Case.objects.all()
    # serializer_class = CaseSerializer
    # permission_classes = [permissions.IsAuthenticated]

#!function 
# @api_view(['GET'])
# def dashboard_overview(request):
#     api_urls = {
#         'List' : '/',
#         'Detail View': '/<str:pk>/',
#         'Create':'/new/',
#         'Update':'/<str:pk>/',
#         'Delete':'/<str:pk>/'
#     }

#     return Response(api_urls)

# @api_view(['GET'])
# def get_user_cases(request):
#     cases = Case.objects.all()
#     serializer = CaseSerializer(cases, many=True)
#     permission_classes = [permissions.IsAuthenticated]


#     return Response(serializer.data)