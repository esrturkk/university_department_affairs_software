from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.ForeignKey("Roles", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.role.title}"


class Roles(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"
    
class Student(User):
    student_no = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.student_no}"