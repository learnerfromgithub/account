# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# class Profile(models.Model):   # apni class ko User mat rakho
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # spelling fix



# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# # Manager
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Email is required")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)  # hash password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         return self.create_user(email, password, **extra_fields)


# # Model
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=150, blank=True, null=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)  # required for admin login

#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []  # jab superuser bnao to email + password hi chalega

#     def __str__(self):
#         return self.email



from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# ---- User Manager ----
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, role="student", **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, role="admin", **extra_fields)


# ---- Custom User Model ----
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # for admin panel access

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []   # only email + password required

    def __str__(self):
        return f"{self.email} ({self.role})"
