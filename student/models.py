from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    admitted_class = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

