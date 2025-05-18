from rest_framework import viewsets
from .models import Plan
from .serializers import PlanSerializer
from rest_framework.filters import OrderingFilter

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    ordering = ['name']


