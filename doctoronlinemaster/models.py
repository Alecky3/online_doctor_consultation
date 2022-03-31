from datetime import date, timedelta, timezone
import datetime
from datetime import time,timedelta
from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.views.generic.list import ListView

class MainSliderImages(models.Model):
    image=models.ImageField(upload_to="mainslider/")
    def __str__(self) :
         return self.image.name

class Partiners(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="ourpartiners/")
    def __str__(self) :
         return self.image.name

class About(models.Model):
    description=models.TextField()
    

class Countries(models.Model):
  id=models.IntegerField(primary_key=True)
  name= models.CharField(max_length=50)
  iso3= models.CharField(max_length=10)
  numeric_code= models.CharField(max_length=10)
  iso2= models.CharField(max_length=5)
  phonecode= models.CharField(max_length=255)
  capital= models.CharField(max_length=100)
  currency=models.CharField(max_length=10)
  currency_symbol= models.CharField(max_length=10)
  tld=models.CharField(max_length=255,blank=True,null=True)
  native= models.CharField(max_length=255,blank=True,null=True)
  region= models.CharField(max_length=255)
  subregion= models.CharField(max_length=255)
  timezones= models.TextField()
  translations= models.TextField()
  latitude=models.DecimalField(max_digits=19,decimal_places=4)
  longitude=models.DecimalField(max_digits=19,decimal_places=4)
  emoji= models.CharField(max_length=200)
  emojiU= models.CharField(max_length=200)
  created_at= models.DateTimeField(auto_now=True)
  updated_at=models.DateTimeField(auto_now=True)
  flag= models.SmallIntegerField(default=1)
  wikiDataId= models.CharField(max_length=255,null=True,blank=True)

  def __str__(self) :
         return self.name

class UserPatient(models.Model):
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=255,unique=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    profile_photo=models.ImageField(upload_to="userpatients/",null=True,blank=True)
    def __str__(self) :
         return self.email

class UserSpecialist(models.Model):
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=255,unique=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    profile_photo=models.ImageField(upload_to="userspecialists/",null=True,blank=True)
    about=models.TextField(blank=True,null=True)
    country=models.CharField(max_length=255,null=True,blank=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    availability=models.BooleanField(default=True)
    specialization=models.ManyToManyField("Specialization")
    online=models.BooleanField(default=True)
    def __str__(self) :
         return self.email
    
    

class Specialization(models.Model):
    SPECIALIZATIO_CHOICES=[
        ("Dr","Doctor"),
        ("Sergion","Sergeon"),
        ("Dentist","Dentist"),
        ("Nurse","Nurse"),
        ("Councillor","Councillor"),
        ("optician","optician"),
         ]
    type=models.CharField(max_length=255,choices=SPECIALIZATIO_CHOICES)
    description=models.TextField()

    def __str__(self) :
      return self.type

class LoginPatient(models.Model):
    userPatient=models.OneToOneField(UserPatient,on_delete=models.CASCADE)
    password=models.CharField(max_length=255)

    def __str__(self) :
         return self.userPatient.email

class SpecialistLogin(models.Model):
    userSpecialist=models.OneToOneField(UserSpecialist,on_delete=models.CASCADE)
    password=models.CharField(max_length=255)

    def __str__(self) :
         return self.userSpecialist.email

class Ambulance(models.Model):
    name=models.CharField(max_length=255,blank=True)
    driver=models.ForeignKey("Driver",on_delete=models.CASCADE,null=True)
    location=models.CharField(max_length=255)
    image=models.ImageField(upload_to="ambulances/")
    available=models.BooleanField(default=True)

class Ambulance_Orders(models.Model):
    ambulance=models.ForeignKey(Ambulance,on_delete=models.CASCADE)
    userPatient=models.ForeignKey(UserPatient,on_delete=models.CASCADE)
    assigned_specialist=models.ForeignKey(UserSpecialist,on_delete=models.CASCADE)
    date_ordered=models.DateTimeField(auto_now=True)
    end_time=models.DateTimeField(default= datetime.datetime.now)

    def endtTime(self):
        return self.date_ordered+timedelta(hours=1,minutes=30)

    
class HomeCare(models.Model):
    supervisor=models.ForeignKey(UserSpecialist,on_delete=models.CASCADE)
    start_date=models.DateField(default=datetime.datetime.now())
    end_date=models.DateField(default=datetime.datetime.now())
    patient=models.ForeignKey(UserPatient,on_delete=models.CASCADE)
    homecareservice=models.ForeignKey("HomeCareServices",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.supervisor.email
    

class HomeCareServices(models.Model):
    type=models.CharField(max_length=255)
    specialist=models.ManyToManyField(UserSpecialist)
    price=models.DecimalField(max_digits=20,decimal_places=4,default=0.00)

    def __str__(self):
        return self.type
   

    
class AppointmentTypes(models.Model):
     type=models.CharField(max_length=255)
     specialist=models.ManyToManyField(UserSpecialist)
     price=models.DecimalField(max_digits=20,decimal_places=4,default=0.00)
     duration=models.TimeField(default=time(1,00))

class Appointment(models.Model):
     fee=models.DecimalField(max_digits=19,decimal_places=4)
     specialist=models.ForeignKey(UserSpecialist,on_delete=models.CASCADE)
     typeOfAppointment=models.CharField(max_length=255)
     start_time=models.DateTimeField(default=timezone.now())
     end_time=models.DateTimeField(default=timezone.now())
     patient=models.ForeignKey(UserPatient,on_delete=models.CASCADE,null=True)
     paid=models.BooleanField(default=False)

     class Meta:
         ordering=["-start_time"]

     def __str__(self) :
         return self.typeOfAppointment


class PatientAppointments(models.Model):
    specialist=models.ForeignKey(UserSpecialist,on_delete=models.CASCADE)
    typeOfAppointment=models.CharField(max_length=255)
    start_time=models.DateTimeField(default=datetime.datetime.now())
    end_time=models.DateTimeField(default=datetime.datetime.now())
    patient=models.ForeignKey(UserPatient,on_delete=models.CASCADE)
    paid=models.BooleanField(default=False)
    fee=models.DecimalField(max_digits=20,decimal_places=4,default=0.00)

    class Meta:
        ordering=["start_time"]

    def __str__(self) :
         return self.typeOfAppointment


class PatientMessages(models.Model):
    user=models.ForeignKey(UserPatient,on_delete=models.CASCADE)
    message=models.TextField()
    datePosted=models.DateTimeField(default=datetime.datetime.now())
    type=models.CharField(max_length=255,default="New Appointment")

class SpecialistMessages(models.Model):
    user=models.ForeignKey(UserSpecialist,on_delete=models.CASCADE)
    message=models.TextField()
    datePosted=models.DateTimeField(default=datetime.datetime.now())
    type=models.CharField(max_length=255,default="New Appointment")

class Driver(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    email=models.EmailField(default="myemail@gmail.com")
    profile_photo=models.ImageField(upload_to="drivers_profile",null=True)





