from pyexpat import model
from django.db import models

# Create your models here.
class User_app(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=70)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    field_of_study = models.CharField(max_length=200)
    phone_of_user = models.CharField(max_length=11)
    email_of_user = models.EmailField()



class Event(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    status_exist = models.BooleanField()
    amount_of_clients_at_event = models.IntegerField()
    phone_of_admin = models.CharField(max_length=11)
    location = models.CharField(max_length=50)
    date_of_start_request = models.DateField()
    date_of_end_request = models.DateField()
    theme = models.CharField(max_length=50 , null=True)
    type = models.CharField(max_length=50 , null=True)
    date_begin = models.DateField()
    date_end = models.DateField()
    

class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User_app, on_delete=models.CASCADE)
    date_joined = models.DateField()
    status = models.CharField(max_length=50)

class Token_and_User(models.Model):
    user_id = models.ForeignKey(User_app, on_delete=models.CASCADE)
    token = models.CharField(max_length=450)

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name_of_image = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')


    

