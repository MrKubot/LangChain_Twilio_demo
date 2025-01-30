from django.db import models

# Create your models here.

class Role(models.TextChoices):
    MAGAZYNIER = ('MGZN', 'Magazynier',)
    BRYGADZISTA = ('BRGD', 'Brygadzista',)
    MANAGER = ('MNGR', 'Manager',)

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=4, choices=Role.choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.get_role_display()}: {self.first_name} {self.last_name} | {self.phone_number}'

