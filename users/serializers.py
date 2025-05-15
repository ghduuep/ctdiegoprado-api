from rest_framework import serializers
from .models import Student, MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    medical_record = MedicalRecordSerializer(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

