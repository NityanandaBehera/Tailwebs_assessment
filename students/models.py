from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    class Meta:
        unique_together = ('name', 'subject', 'teacher')

    def __str__(self):
        return f"{self.name} - {self.subject}"
