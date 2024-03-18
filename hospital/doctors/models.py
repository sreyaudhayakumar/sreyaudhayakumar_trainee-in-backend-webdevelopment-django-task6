from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Person(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
