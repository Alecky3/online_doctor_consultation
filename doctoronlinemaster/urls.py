from django.urls import path
from .views import *

app_name="doctoronlinemaster"

urlpatterns=[
    path("",homeView,name="home"),
    path("patientlogin/",patientLogin,name="patientlogin"),
    path("doctorlogin/",doctorLogin,name="doctorlogin"),
    path("signup/",signupView,name="signup"),
    path("login/",login,name="login"),
    path("signuppatient/",signUpViewPatient,name="signuppatient"),
    path("dashboard/<int:user_id>/",dashboard,name="dashboard"),
    path("userdashboard/<int:user_id>/",userDashboard,name="userdashboard"),
    path("getJson/",getJson,name="getjson"),
    path("getJsonTest/",getJsonView,name="getJsonTest"),
    path("getspecialist/",getSpecialist,name="getspecialist"),
    path("makeappointment/",makeAppointment,name="makeappointment"),
    path("deletepatientmessage/",deletePatientMessage,name="deletepatientmessage"),
    path("deletePatientAppointment/",deletePatientAppointment),
    path("ambulancedetails/",getAmbulanceDetails),
    path("bookambulance/",bookAmbulance),
]