from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, DashboardStatusView

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register(r'dashboard-status', DashboardStatusView, basename='dashboard-status')
urlpatterns = router.urls