from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.


class About(models.Model):
    user = models.ForeignKey(User, default=1)
    name=models.CharField(max_length=200)
    position = models.CharField(max_length=250)
    dept = models.CharField(max_length=500)
    college = models.CharField(max_length=100)
    image = models.FileField()
    intro = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    telephone = models.IntegerField()
    officeaddress = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Edu(models.Model):
    user = models.ForeignKey(User, default=1)
    institute=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    timeperiod=models.CharField(max_length=100)

    def __str__(self):
        return self.institute

class Teaching(models.Model):
    user=models.ForeignKey(User,default=1)
    course=models.CharField(max_length=100)
    currentorpast=models.CharField(max_length=10)

    def __str__(self):
        return self.course

class Experience(models.Model):
    user = models.ForeignKey(User, default=1)
    position=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)
    timeperiod=models.CharField(max_length=100)

    def __str__(self):
        return self.position

class Todolist(models.Model):
    class Meta:
        ordering = ['month','date']
    user=models.ForeignKey(User, default=1)
    reminder=models.CharField(max_length=200)
    date=models.IntegerField(max_length=2)
    month=models.IntegerField(max_length=2)


