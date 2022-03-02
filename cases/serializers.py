from .models import Appointment
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'name']