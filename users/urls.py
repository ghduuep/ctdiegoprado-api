from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'medical-records', MedicalRecordViewSet, basename='medical-records')
urlpatterns = router.urls