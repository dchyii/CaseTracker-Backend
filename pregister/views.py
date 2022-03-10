from xmlrpc.client import ResponseError
from django.shortcuts import render
from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Case, Step, UserDetails
from django.contrib.auth.models import User
from .serializers import CaseSerializer, StepSerializer, UserDetailsSerializer

# Create your views here.
class CaseListView(ListCreateAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(staffer=self.request.user)

    def get_queryset(self):
        print("get request")
        # user = User.objects.filter(username=self.request.user)
        # print(user)
        # return Case.objects.filter(Q(steps__staffer=self.request.user) | Q(steps__res_party=self.request.user))
        return Case.objects.filter(steps__res_party=self.request.user).distinct()


class CaseDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        print(self.request.data)
        return Case.objects.filter(Q(staffer=self.request.user) | Q(current_res_party=self.request.user))

class StepListView(ListCreateAPIView):
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(staffer=self.request.user)
    
    def get_queryset(self):
        return Step.objects.filter(Q(staffer=self.request.user) | Q(res_party=self.request.user))

class StepDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field="id"
    
    def get_queryset(self):
        return Step.objects.filter(Q(staffer=self.request.user) | Q(res_party=self.request.user))

class DomainMembersView(ListCreateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_model = User.objects.get(username=self.request.user)
        user_details_model = UserDetails.objects.get(user=user_model.id)
        domain_id = user_details_model.domain.id
        dir_appointment_id = 4
        print(domain_id)
        return UserDetails.objects.filter(Q(domain=domain_id) | Q(appointment=dir_appointment_id))
