from rest_framework import serializers 
from .models import Case, Step

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
