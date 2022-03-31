from django.core.checks import messages
from django.http import response
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Ambulance, Ambulance_Orders, Appointment, AppointmentTypes, HomeCare, HomeCareServices, MainSliderImages,Partiners,About, PatientAppointments,Specialization,UserPatient,LoginPatient,Countries,UserSpecialist,SpecialistLogin,PatientMessages,SpecialistMessages
from django.urls import reverse
import requests
import datetime
from datetime import time,timedelta,date
import random

def homeView(request):
    mainsliderimages=MainSliderImages.objects.all()
    partiners=Partiners.objects.all()
    about=About.objects.all()
    if about.count() > 0 :
          doctoronlineabout=about[0]
    else:
         doctoronlineabout="Add Description About Your Platform so as users to Know You better."
    return render(request,"doctoronlinemaster/main.html",
    {"mainsliderimages":mainsliderimages,"partiners":partiners,"about":doctoronlineabout,})

def patientLogin(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if email and password:
            try:
                userPatient=UserPatient.objects.get(email=email)
                userPatientLogin=LoginPatient.objects.get(userPatient=userPatient,password=password)
            except UserPatient.DoesNotExist:
                loginerrorMsg="Such user Does not exist. Create an Account to Access our Services"
                return  render(request,"doctoronlinemaster/login.html",{"loginErrorMsg":loginerrorMsg,})
            except LoginPatient.DoesNotExist:
                loginerrorMsg="Password Incorrect. Try Again or Reset Password"
                return  render(request,"doctoronlinemaster/login.html",{"loginErrorMsg":loginerrorMsg,})
            else:
                return HttpResponseRedirect(reverse("doctoronlinemaster:userdashboard",args=(userPatient.pk,)))

    return render(request,"doctoronlinemaster/login.html")

def doctorLogin(request):
    if request.method == "POST":
        email=request.POST.get("doctor_email")
        password=request.POST.get("doctor_password")
        if email and password:
            try:
                userSpecialist=UserSpecialist.objects.get(email=email)
                userPatientLogin=SpecialistLogin.objects.get(userSpecialist=userSpecialist,password=password)
            except UserSpecialist.DoesNotExist:
                loginerrorMsg="Such user Does not exist. Create an Account to Access our Services"
                return  render(request,"doctoronlinemaster/login.html",{"loginErrorMsg":loginerrorMsg,})
            except SpecialistLogin.DoesNotExist:
                loginerrorMsg="Password Incorrect. Try Again or Reset Password"
                return  render(request,"doctoronlinemaster/login.html",{"loginErrorMsg":loginerrorMsg,})
            else:
                return HttpResponseRedirect(reverse("doctoronlinemaster:dashboard",args=(userSpecialist.pk,)))

    return render(request,"doctoronlinemaster/login.html")


def signUpViewPatient(request):
    countries=[country.name for country in Countries.objects.all()]
    cities=[country.capital for country in Countries.objects.all() ]
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user=UserPatient.objects.get(email=email)
            if user:
                usererror="User Already Exists. Reset Password or create another account with another Email"
                return render(request,"doctoronlinemaster/signup.html",{"usererror":usererror,"countries":countries,"cities":cities,})
        except UserPatient.DoesNotExist:
            if email and  password :
                userPatient=UserPatient(email=email)
                userPatient.save()
                userPatientLogin=LoginPatient(userPatient=userPatient,password=password)
                userPatientLogin.save()
                return HttpResponseRedirect(reverse("doctoronlinemaster:userdashboard",args=(userPatient.pk,)))
    
    return render(request,"doctoronlinemaster/signup.html",{"currentindex":False,"countries":countries,"cities":cities})
    
def signupView(request):
    countries=[country.name for country in Countries.objects.all()]
    cities=[country.capital for country in Countries.objects.all() ]
    if request.method=="POST":
        fname=request.POST.get("doctor_fname")
        lname=request.POST.get("doctor_lname")
        email=request.POST.get("doctor_email")
        password=request.POST.get("doctor_password")
        country=request.POST.get("country")
        city=request.POST.get("city")
        phone=request.POST.get("doctor_phone")
        try:
            user=UserSpecialist.objects.get(email=email)
            if user:
                usererror="User Already Exists. Reset Password or create another account with another Email"
                return render(request,"doctoronlinemaster/signup.html",{"currentindex":True,"usererror":usererror,"countries":countries,"cities":cities,})
        except UserSpecialist.DoesNotExist:

            if email and  password :
               userSpecialist=UserSpecialist(first_name=fname,last_name=lname,email=email,country=country,city=city,phone=phone)
               userSpecialist.save()
               userSpecialistLogin=SpecialistLogin(userSpecialist=userSpecialist,password=password)
               userSpecialistLogin.save()
               return HttpResponseRedirect(reverse("doctoronlinemaster:dashboard",args=(userSpecialist.pk,)))
    
    return render(request,"doctoronlinemaster/signup.html",{"currentindex":False,"countries":countries,"cities":cities})

def login(request):
    return render(request,"doctoronlinemaster/login.html")

## specialist dashboard
def dashboard(request,user_id):
     
     user=UserSpecialist.objects.get(pk=user_id)
     try:
         profile_img=user.profile_photo.url
         profile_img=True
     except:
         profile_img=False

     assignedambulances=Ambulance_Orders.objects.filter(assigned_specialist=user)
     allhomecareservices=HomeCare.objects.filter(supervisor=user)
     activehomecare=HomeCare.objects.filter(supervisor=user).filter(end_date__gte=date.today())
     activeassignedambulances=Ambulance_Orders.objects.filter(assigned_specialist=user).filter(end_time__gte=datetime.datetime.now())
     activeappointments=Appointment.objects.filter(specialist=user).filter(end_time__gte=datetime.datetime.now())
     allappointments=Appointment.objects.filter(specialist=user)
     return render(request,"doctoronlinemaster/dashboard.html",
     {"activeappointments":activeappointments,"allappointments":allappointments,
     "assignedambulances":assignedambulances,"activeassignedambulances":activeassignedambulances,
     "allhomecareservices":allhomecareservices,"activehomecare":activehomecare,"profile_img":profile_img,"user":user,})

##end of specialist dashboard

def userDashboard(request,user_id):
    specialists={}
    
    user=UserPatient.objects.get(pk=user_id)
    messages=PatientMessages.objects.filter(user=user).order_by("-datePosted")
    ambulances=Ambulance.objects.all()
    allhomecareservices=HomeCare.objects.filter(patient=user)
    activehomecareservices=HomeCare.objects.filter(end_date__gte=date.today())
    allambulanceorders=Ambulance_Orders.objects.filter(userPatient=user)
    currentamulanceorder=Ambulance_Orders.objects.filter(userPatient=user).filter(end_time__gte=datetime.datetime.now())
    appointments=PatientAppointments.objects.filter(patient=user)
    activeappointments=PatientAppointments.objects.filter(end_time__gte=datetime.datetime.now()).order_by("start_time")

    for sc in Specialization.objects.all():
        if sc.userspecialist_set.all().count() > 0:
            specialists[sc.type]=sc.userspecialist_set.all()
    return render(request,"doctoronlinemaster/userdashboard.html",{"specialists":specialists,"ambulances":ambulances,
    "user":user,"messages":messages,"appointments":appointments,"activeappointments":activeappointments,
    "ambulanceorders":allambulanceorders,"activeambulanceorders":currentamulanceorder,
    "allhomecareservices":allhomecareservices,"activehomecareservices":activehomecareservices,})


def getSpecialist(request):
     specialist_id=request.GET["specialist_id"]
     try:
         specialist=UserSpecialist.objects.get(pk=specialist_id)
         f_name=specialist.first_name
         l_name=specialist.last_name
         phone=specialist.phone
         email=specialist.email
         about=specialist.about
         country=specialist.country
         city=specialist.city
         specialization=[]
         typeOfAppointment=[[sp.type,sp.price,sp.pk] for sp in AppointmentTypes.objects.filter(specialist=specialist)]
         activeappointments=[sp.end_time for sp in specialist.appointment_set.filter(end_time__gte=datetime.datetime.now())]
         
         
         for s in specialist.specialization.all():
                specialization.append(s.type)
         specialistDetails={
            "first_name":f_name,
            "last_name":l_name,
            "email":email,
            "phone":phone,
            "about":about,
            "country":country,
            "city":city,
            "specialization":specialization,
            "active_appointments":activeappointments,
            "typeOfAppointment":typeOfAppointment
        }
         return JsonResponse({"specialistData":specialistDetails},safe=False)
     except UserSpecialist.DoesNotExist:
         return JsonResponse({"data":"none"},safe=False)

    
def makeAppointment(request):
    sId=request.POST.get("specialist_id")
    apType=request.POST.get("appointment_type")
    apId=request.POST.get("appointment_id")
    apPrice=request.POST.get("appointment_price")
    pEmail=request.POST.get("patient_email")
    print(request.POST)
    try:
      sp=UserSpecialist.objects.get(pk=sId)
      print("got specialist")
      up=UserPatient.objects.get(email=pEmail)
      print("got patient")
      appointementTime=AppointmentTypes.objects.get(pk=apId).duration
      print("got appointment time")
      if Appointment.objects.all().count() > 0:
         print("in if")
         drApp=Appointment.objects.filter(end_time__gte=datetime.datetime.now()).order_by("-end_time")[0].end_time
         print("after if")
      else:
         drApp=datetime.datetime.now()
         print("got appointment")
      
      print("last_appointment: ",drApp)
      app=Appointment(specialist=sp,fee=apPrice,typeOfAppointment=apType,patient=up,start_time=drApp,end_time=drApp+timedelta(hours=appointementTime.hour,minutes=appointementTime.minute+20))
      app.save()

      papp=PatientAppointments(specialist=sp,fee=apPrice,typeOfAppointment=apType,patient=up,start_time=drApp,end_time=drApp+timedelta(hours=appointementTime.hour,minutes=appointementTime.minute+20))
      papp.save()
      print("")
      pm=PatientMessages(user=up,
      message="Made an a {0} appointment with\n {1} \nmore details to be send to your email.".format(apType,sp.first_name+" "+sp.last_name+"\n"+sp.email))
      pm.save()
      sm=SpecialistMessages(user=sp,
       message="{0} Requested a {1} appointment with you at \n {2}".format(sp.first_name+" "+sp.last_name+"\n"+sp.email+"\n",apType,datetime.datetime.now())
      )
      sm.save()
      print("after save specialist message.")
      data={
          "appointmentType":apType,
          "message_id":pm.pk,
          "datePosted":pm.datePosted,
          "message":pm.message,
          "specialist_email":sp.email,
          "start_time":papp.start_time,
           "end_time":papp.end_time,
           "appointment_id":papp.pk
      }
      return JsonResponse({"success":True,"data":data},safe=False)
    except:
     return JsonResponse({"success":False,})
def deletePatientAppointment(request):
    apId=request.POST.get("appointment_id")
    try:
        ap=PatientAppointments.objects.get(pk=apId)
        ap.delete()
        return JsonResponse({"deleted":True},safe=False)
    except:
        return JsonResponse({"deleted":False},safe=False)

def deletePatientMessage(request):
      msgId=request.POST.get("message_id")
      try:
        msg=PatientMessages.objects.get(pk=msgId)
        msg.delete()
        return JsonResponse({"deleted":True},safe=False)
      except:
          return JsonResponse({"deleted":False},safe=False)

def getJsonView(request):
    return render(request,"doctoronlinemaster/ajax.html")

def getAmbulanceDetails(request):
    ambulanceId=request.GET.get("ambulance_id")
    try:
        ambulance=Ambulance.objects.get(pk=ambulanceId)
        ambulanceDetails={}
        ambulanceDetails["plate"]=ambulance.name
        ambulanceDetails["driver_name"]=ambulance.driver.name
        ambulanceDetails["driver_phone"]=ambulance.driver.phone
        ambulanceDetails["driver_email"]=ambulance.driver.email
        ambulanceDetails["driver_photo"]=ambulance.driver.profile_photo.url
        return JsonResponse({"data":ambulanceDetails},safe=False)
    except:
        return JsonResponse({"data":"unable to fetch ambulance deteils"})

def bookAmbulance(request):
    ambulanceId=request.POST.get("ambulance_id")
    userId=request.POST.get("user_id")
    print("got ids: ",ambulanceId,userId)
    try:
        ambulance=Ambulance.objects.get(pk=ambulanceId)
        userPatient=UserPatient.objects.get(pk=userId)
        print("got entities: ",ambulance,userPatient)
        spNo=random.randrange(UserSpecialist.objects.all().count()-1)
        specialist=UserSpecialist.objects.all()[spNo]
        print("got specialist: ",specialist)
        ambulanceOrder=Ambulance_Orders(ambulance=ambulance,userPatient=userPatient,assigned_specialist=specialist)
        print("after ambulance")
        ambulanceOrder.save()
        pm=PatientMessages(user=userPatient,message="Booked ambulance at {0}.".format(datetime.datetime.now()),type="Emergency services")
        pm.save()
        sm=SpecialistMessages(user=specialist,message="Placed for  ambulance services  at {0}.".format(datetime.datetime.now()),type="Emergency services")
        sm.save()
        return JsonResponse({"data":"Booked Ambulance at {0} plate {1}".format(datetime.datetime.now(),ambulance.name)})
    except:
        return JsonResponse({"data":"Cannot book the requested ambulance now."})
        


def getJson(request):
    # response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' })
    # print(response.text.encode('utf8'))
    response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' })
    print(response.text.encode('utf8'))
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer aF4gB35tJfhW3GSVM5QEx0jvvUA3'
}
    payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjExMDA5MTIyNjE4",
    "Timestamp": "20211009122618",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254740500532,
    "PartyB": 174379,
    "PhoneNumber": 254740500532,
    "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
    "AccountReference": "ALEXMUTHINI",
    "TransactionDesc": "Payment of X" 
  }
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    print(response.text.encode('utf8'))
    return JsonResponse({"about":response.text},safe=False)

   
            