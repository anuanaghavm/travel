from django.db import models

class register(models.Model):
    USERNAME = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50)
    PHONENUMBER = models.IntegerField()
    PASSWORD = models.IntegerField()
    CONFIRMPASSWORD = models.IntegerField()
    def __str__(self):
        return self.USERNAME


class login(models.Model):
    USERNAME = models.CharField(max_length=50)
    PASSWORD = models.IntegerField()
    status=models.IntegerField()
    def __str__(self):
        return self.USERNAME

class booking(models.Model):
    NAME = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50)
    PHONENUMBER = models.IntegerField()
    PLACE = models.CharField(max_length=200)
    PEOPLE = models.IntegerField()
    PROOF = models.IntegerField()
    AMOUNT=models.IntegerField()
    def __str__(self):
        return self.NAME

class buss(models.Model):
    NAME = models.CharField(max_length=50)
    PHONENUMBER = models.IntegerField()
    TO = models.CharField(max_length=100)
    FROM = models.CharField(max_length=100)
    PEOPLE = models.IntegerField()
    AMOUNT = models.IntegerField()
    def __str__(self):
        return self.NAME

# Create your models here.
