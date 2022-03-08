from .models import Appointment, Domain, Team, UserDetails, Planning, Bidding, Approval, Contracting, Case, Comment
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_staff", "is_active"]

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'name']

class DomainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'name']

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        # fields = ["id", "staffer", "vetter", "supporter1", "supporter2"]
        fields = '__all__'

class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class PlanningSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planning
        fields = '__all__'

class BiddingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bidding
        fields = '__all__'

class ApprovalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'

class ContractingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contracting
        fields = '__all__'

class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class DashboardSerializer(serializers.HyperlinkedModelSerializer):
    # cases = serializers.StringRelatedField(many=True)
    # print(cases)
    staffer = serializers.StringRelatedField(many=False)
    current_step_user = serializers.StringRelatedField(many=False)
    next_step_user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Case
        fields = '__all__'

        depth = 1