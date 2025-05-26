from rest_framework import viewsets
from .models import Subscription
from .serializers import SubscriptionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication




class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.select_related('student', 'plan').all()
    serializer_class = SubscriptionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['plan', 'status']
    search_fields = ['student__first_name', 'student__last_name']
    ordering = ['start_date']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

