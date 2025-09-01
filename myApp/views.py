from django.shortcuts import render,redirect, get_object_or_404
from myApp.models import Doctor ,Patient  # ✅ yahan .models use karna hai (na ke myApp.models)

def doctor_view(request):
    doctor = Doctor.objects.all()
    return render(request, 'table.html', {'d': doctor})

def add_doctor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        specialization = request.POST.get("specialization")
        Doctor.objects.create(name=name, specialization=specialization)
        return redirect("doctor_view")  # ✅ ab redirect karega list wale page par

    return render(request, "doctor_list.html") 



def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.name = request.POST.get("name")
        doctor.specialization = request.POST.get("specialization")
        doctor.save()
        return redirect("doctor_view")  # redirect after update
    return render(request, "update_doctor.html", {"doctor": doctor})

# Delete doctor
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return redirect("doctor_view")
 # ✅ form alag page


 
def patient_view(request):
    pat = Patient.objects.all()
    return render(request ,'home.html',{'p':pat} )
def add_patient(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        disease = request.POST.get('disease')
        
        Patient.objects.create(name=name, age=age, disease=disease)
        
        return redirect('patient_view')   # ✅ Ab ye chalega
    return render(request, 'patient_list.html')