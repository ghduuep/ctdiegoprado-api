from rest_framework import viewsets
from .models import Plan
from .serializers import PlanSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]




