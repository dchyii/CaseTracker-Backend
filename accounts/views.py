from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# from cases.models import Domain, UserDetails, Appointment
from pregister.models import Domain, UserDetails, Appointment

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_model = User.objects.get(username=user)
        print(user_model.first_name)
        print(user_model.email)
        user_details_model = UserDetails.objects.get(user=user_model.id)
        print(user_details_model)
        domain = user_details_model.domain.name
        appointment = user_details_model.appointment.name
        first_name = user_model.first_name
        email = user_model.email


        # Add custom claims
        token['username'] = user.username
        token['appointment'] = str(appointment)
        token['domain'] = str(domain)
        token['firstName'] = str(first_name)
        token['email'] = str(email)
        # ...

        return token

# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer