from django.db import models
from users.models import Student
from plans.models import Plan
from django.utils import timezone

class Subscription(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativa'),
        ('paused', 'Pausada'),
        ('canceled', 'Cancelada'),
        ('expired', 'Vencida')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subscriptions', unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='subscriptions')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    class Meta:
        unique_together = ('student', 'plan', 'start_date')

    def __str__(self):
        return f"{self.student.name} - {self.plan.name} ({self.status})"