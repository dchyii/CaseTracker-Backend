from django.shortcuts import render
from .models import Appointment
from rest_framework import viewsets, permissions
from .serializers import AppointmentSerializer

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_class = [permissions.AllowAny]