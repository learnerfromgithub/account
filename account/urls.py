from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),   # 👈 fixed
    path("logout/", views.logout_view, name="logout"),



    #   path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    # path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    # path("student/dashboard/", views.student_dashboard, name="student_dashboard"),

]
