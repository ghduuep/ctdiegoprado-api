from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Student
from django.db.models import Count, Q, Sum
from rest_framework.response import Response
from rest_framework import status
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

class DashboardStatusView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        total_clientes = Student.objects.count()

        subscription_stats = Subscription.objects.aggregate(
            active = Count('id', filter=Q(status='active')),
            paused = Count('id', filter=Q(status='paused')),
            expired = Count('id', filter=Q(status='expired'))
        )

        data = {
            'totalClientes': total_clientes,
            'mensalidadesAtivas': subscription_stats.get('active', 0),
            'mensalidadesPausadas': subscription_stats.get('paused', 0),
            'mensalidadesExpiradas': subscription_stats.get('expired', 0)
        }

        return Response(data, status=status.HTTP_200_OK)
    
class FinancialSummaryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        total_subscriptions_data = Subscription.objects.filter(status='active').aggregate(
            total_subscriptions = Sum('plan__price')
        )

        total_subscriptions = total_subscriptions_data['total_subscriptions'] or 0.00
        
        data = {
            'total_mensalidades_ativas': total_subscriptions
        }

        return Response(data, status=status.HTTP_200_OK)
