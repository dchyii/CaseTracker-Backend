from rest_framework import serializers 
from .models import Case, Domain, Step, Appointment, UserDetails
from django.contrib.auth.models import User

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'
        

class CaseSerializer(serializers.ModelSerializer):
    # steps = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True
    # )
    steps = StepSerializer(many=True, read_only=True)
    
    class Meta:
        model = Case
        fields = '__all__'

        # depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment 
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    appointment = AppointmentSerializer(many=False, read_only=True)
    domain = DomainSerializer(many=False, read_only=True)

    class Meta:
        model = UserDetails
        fields = '__all__'
