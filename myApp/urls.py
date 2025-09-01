from django.urls import path
from . import views

urlpatterns = [
    
   
    path('doc/', views.doctor_view, name='doctor_view'),
    path("doctor/update/<int:id>/", views.update_doctor, name="update_doctor"),
    path("doctor/delete/<int:id>/", views.delete_doctor, name="delete_doctor"),
    path('doc/add/', views.add_doctor, name='add_doctor'),
    
    path('pat/add/', views.add_patient, name='add_patient'),
     path('pat/', views.patient_view, name='patient_view'),   

]
