from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre asignatura')
    course = models.CharField(max_length=100, verbose_name='Curso')
    pass_rate = models.FloatField(verbose_name='Tasa de aprobados')

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Nombre')
    dni =  models.CharField(max_length=9, verbose_name='DNI')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Imagen de perfil')
    coins = models.FloatField(default=0)
    current_subjects = models.ManyToManyField(Subject, verbose_name='Asignaturas matriculadas')
    passed_subjects = models.ManyToManyField(Subject, verbose_name='Asignaturas aprobadas', related_name='passed_subjects')

    def __str__(self):
        return self.name + ' ' + self.user.first_name + ' ' + self.user.last_name + ' (' + self.user.username + ')'
