from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre asignatura')
    course = models.CharField(max_length=100, verbose_name='Curso')
    pass_rate = models.FloatField(verbose_name='Tasa de aprobados')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

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

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

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