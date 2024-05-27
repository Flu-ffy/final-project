#from django.db import models
#from django.contrib.auth.models import BaseUserManager

# Create your models here.
# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("The email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using= self.db)
#         return user
