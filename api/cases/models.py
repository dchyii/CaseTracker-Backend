from django.db import models

# Create your models here.
class Appointment(models.Model):
    APPOINTMENTS = (
        ('staffer', 'Staffer'),
        ('manager', 'Manager'),
        ('deputy director', 'Deputy Director'),
        ('director', 'Director')
    )
    name = models.CharField(max_length=20, choices=APPOINTMENTS)