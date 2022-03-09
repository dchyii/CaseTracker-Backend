from django.shortcuts import render
from django.db.models import Q
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Case, Step
from django.contrib.auth.models import User
from .serializers import CaseSerializer, StepSerializer

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
        return Case.objects.filter(Q(staffer=self.request.user) | Q(current_res_party=self.request.user))

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
