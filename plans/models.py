from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    duration_months = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

