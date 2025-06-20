from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, DashboardStatusView, FinancialSummaryView
from django.urls import path, include

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard-status/', DashboardStatusView.as_view(), name='dashboard-status'),
    path('financial-summary/', FinancialSummaryView.as_view(), name='financial-summary')
]