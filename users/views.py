from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().prefetch_related('subscriptions__plan')
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'phone']
    ordering = ['first_name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]