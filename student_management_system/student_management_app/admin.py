from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CustomUser
# Register your models here.

# Creating blank UserModel class and registering into admin.py of our app to encrypt the
# passwords

class UserModel(UserAdmin):

    pass

admin.site.register(CustomUser, UserModel)
