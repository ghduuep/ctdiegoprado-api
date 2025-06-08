from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    plan_name = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ['id', 'student', 'plan', 'start_date', 'end_date', 'status', 'student_name', 'plan_name']
    
    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

    def get_plan_name(self, obj):
        return obj.plan.name

