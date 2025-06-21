from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    birthday_date = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalRecord(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='medical_record')

    has_heart_problems = models.BooleanField(default=False)
    has_joint_pain = models.BooleanField(default=False)
    takes_medication = models.BooleanField(default=False)
    had_surgeries = models.BooleanField(default=False)
    smokes = models.BooleanField(default=False)
    drinks_alcohol = models.BooleanField(default=False)
    practices_physical_activity = models.BooleanField(default=False)
    physical_activity_frequency = models.CharField(max_length=100, blank=True, default='')
    fitness_goals = models.TextField(blank=True, null=True, default='')
    medical_restrictions = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return f'Registro médico de {self.student.first_name} {self.student.last_name}'