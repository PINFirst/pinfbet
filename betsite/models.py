from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre asignatura')
    course = models.CharField(max_length=100, verbose_name='Curso')
    pass_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)],
                                  verbose_name='Tasa de aprobados')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'


def get_default_profile_image():
    return "images/default.jpg"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Imagen de perfil')
    coins = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    current_subjects = models.ManyToManyField(Subject, verbose_name='Asignaturas matriculadas')
    passed_subjects = models.ManyToManyField(Subject, blank=True, verbose_name='Asignaturas aprobadas',
                                             related_name='passed_subjects')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' (' + self.user.username + ')'

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


class Bet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Alumno')
    friend = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True, related_name='friend',
                               verbose_name='Amigo apostado')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Asignatura')
    bet_grade = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)],
                                    verbose_name='Nota apostada')
    actual_grade = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                       verbose_name='Nota sacada')
    coins = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha apuesta')
    end_date = models.DateTimeField(verbose_name='Fecha fin de apuesta')

    def __str__(self):
        return self.student.user.username + ' ' + self.start_date.strftime("%d/%m/%Y %H:%M:%S")

    class Meta:
        verbose_name = 'Apuesta'
        verbose_name_plural = 'Apuestas'


class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, user):

        if user not in self.friends.all():
            self.friends.add(user)
            self.save()

    def remove_friend(self, user):

        if user in self.friends.all():
            self.friends.remove(user)

    def unfriend(self, removee):

        remover_friends_list = self
        remover_friends_list.remove_friend(removee)

        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(remover_friends_list.user)

    def is_mutual_friend(self, friend):

        if friend in self.friends.all():
            return True
        return False


class FriendRequest(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")

    is_active = models.BooleanField(blank=False, null=False, default=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        self.is_active = False
        self.save()

    def cancel(self):
        self.is_active = False
        self.save()
