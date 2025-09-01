# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages

# # Register View
# def register(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists")
#             return redirect("register")

#         user = User.objects.create_user(username=email, email=email, password=password)  # 👈 username = email
#         user.save()
#         messages.success(request, "Account created successfully! Please login.")
#         return redirect("login")

#     return render(request, "register.html")


# # ✅ Login View (renamed)
# def login_view(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             auth_login(request, user)   # 👈 yahan auth_login use kiya hai
#             return redirect("patient_view")
#      # apna home url name yahan daalo
#         else:
#             messages.error(request, "Invalid username or password")

#     return render(request, "login.html")


# def logout_view(request):
#     logout(request)
#     return redirect("login")




from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        user = CustomUser.objects.create_user(email=email, password=password, role=role)
        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "register.html")




def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            if user.role == "admin":
                return redirect("admin_dashboard")
            elif user.role == "doctor":
                return redirect("doctor_view")
            elif user.role == "patient":
                return redirect("patient_view")
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, "login.html")



def logout_view(request):
    logout(request)
    return redirect("login")
