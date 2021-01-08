from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(User):
    hide_email = models.BooleanField(default=True)


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre asignatura')
    course = models.CharField(max_length=100, verbose_name='Curso')
    pass_rate = models.FloatField(verbose_name='Tasa de aprobados')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'


class Grade(models.Model):
    int_grade = models.IntegerField()
    float_grade = models.FloatField()
    range_grade = models.TextChoices('RangeGrade', 'INSUFICIENTE SUFICIENTE BIEN NOTABLE SOBRESALIENTE')

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

class Bet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Alumno')
    friend = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='friend', verbose_name='Amigo apostado')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Asignatura')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='Nota apostada')
    coins = models.FloatField()
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha apuesta')
    end_date = models.DateTimeField(verbose_name='Fecha fin de apuesta')

    class Meta:
        verbose_name = 'Apuesta'
        verbose_name_plural = 'Apuestas'

