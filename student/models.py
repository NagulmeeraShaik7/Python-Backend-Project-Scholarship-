from django.db import models

# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=30)
    hallticket = models.CharField(max_length=30)
    clgname = models.CharField(max_length=30)
    aadharno = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.fullname},{self.hallticket},{self.clgname}"
