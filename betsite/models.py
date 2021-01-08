from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(User):
    hide_email = models.BooleanField(default=True)


