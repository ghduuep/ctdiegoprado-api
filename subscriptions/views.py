from rest_framework import viewsets
from .models import Subscription
from .serializers import SubscriptionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.select_related('student', 'plan').all()
    serializer_class = SubscriptionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['plan__name', 'status']
    search_fields = ['student__first_name', 'student__last_name']

