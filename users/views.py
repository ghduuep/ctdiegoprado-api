from rest_framework import viewsets
from .models import Student, MedicalRecord
from .serializers import StudentSerializer, MedicalRecordSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().prefetch_related('subscriptions__plan')
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'phone']
    ordering = ['first_name']


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student']
    