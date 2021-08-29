from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

class Person(models.Model):
    firstName = models.CharField(max_length=120, unique=True)
    lastName = models.CharField(max_length=120, unique=True)
    
    def _str_(self):
        return self.firstName


class PayCheck(models.Model):
    name = models.CharField(max_length=200)
    hourly = models.IntegerField()
    totalHours = models.IntegerField()
    grossPay = models.IntegerField()
    def grossPay(self):
        return self.hourly * self.totalHours
    def __str__(self):
        return self.name