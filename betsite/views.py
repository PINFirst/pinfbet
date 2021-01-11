from django.shortcuts import render, redirect
from django import forms
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from datetime import datetime
import json
from .database import data_posts, data_users


def time_ago_aux(ago, cal):
    return (ago, cal) if ago == 1 else (ago, cal + 's')


def time_ago(date):
    now = datetime.now()

    number = 0
    cal = 'parsecs'

    if now.year > date.year:
        years_ago = now.year - date.year
        number, cal = time_ago_aux(years_ago, 'year')
    elif now.month > date.month:
        months_ago = now.month - date.month
        number, cal = time_ago_aux(months_ago, 'month')
    elif now.day > date.day:
        days_ago = now.day - date.day
        number, cal = time_ago_aux(days_ago, 'day')

    elif now.hour > date.hour:
        hours_ago = now.hour - date.hour
        number, cal = time_ago_aux(hours_ago, 'hour')

    elif now.minute > date.minute:
        minutes_ago = now.minute - date.minute
        number, cal = time_ago_aux(minutes_ago, 'minute')

    else:
        seconds_ago = now.second - date.second
        number, cal = time_ago_aux(seconds_ago, 'second')

    time_msg = '{} {} ago'.format(number, cal)

    return time_msg


def get_user_id(user_name):
    for user in data_users['users']:
        if user['user_name'] == user_name:
            return user['id']

    return None


def get_user():
    user = {}
    user['name'] = 'Jeff'
    user['profile_img'] = 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg'
    return user


def get_post(post_id):
    for post in data_posts['posts']:
        if post['id'] == post_id:
            return post

    return None


class HandleLike(View):

    def post(self, request):
        request_data = json.loads(request.body)
        user_id = get_user_id(request_data['user'])
        post = get_post(request_data['post'])
        print(post)
        if user_id in post['likes']:
            post['likes'].remove(user_id)
        elif user_id not in post['likes']:
            post['likes'].append(user_id)

        print(post)

        return HttpResponse(request)


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        surnames = form.cleaned_data.get("surnames")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.first_name = name
        newUser.last_name = surnames
        newUser.email = email
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        return redirect("Feed")
    return render(request, 'SignUp.html', {'form': form})


class Terms(View):
    template = 'Terms.html'

    def get(self, request):
        return render(request, self.template)


class Profile(View):
    template = 'profile/profile.html'

    def get(self, request):
        return render(request, self.template)


class Feed(View):
    template = 'feed/feed.html'

    def get(self, request):
        return render(request, self.template)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.info(request, 'Usuario o contraseña incorrectas')
            print('Usuario incorrecto')

    return render(request, 'login.html')


class GetPosts(View):
    def get(self, request, page=0):
        posts = data_posts['posts']
        post_paginated = posts[page:page + 5]

        return HttpResponse(json.dumps(post_paginated), content_type="application/json")


class SendPost(View):
    def post(self, request):
        user = get_user()
        owner = 1

        request_data = json.loads(request.body)
        print(request_data)

        today = datetime.now()

        time_message = time_ago(today)

        if request_data['type'] == 'bet':
            post = {
                'id': len(data_posts['posts']) + 1,
                'owner': owner,
                'likes': [],
                'User': request_data['user'],
                'profile_img': user['profile_img'],
                'message': request_data['message'],
                'type': request_data['type'],
                'bet': request_data['bet'] + ' ' + request_data['subject'] + ' con un ' + request_data['grade'],
                'coins': request_data['coins'],
                'time': time_message,
                'image': None,
                'image_url': None,
                'comments': [
                ]
            }

            data_posts['posts'].insert(0, post)

        return HttpResponse(request)


class Comment(View):
    def post(self, request):
        print(request.body)
        return HttpResponse(request)


class DeleteComment(View):
    def post(self, request):
        print("Eliminado comentario ", request.body)
        return HttpResponse(request)


class DeletePost(View):
    def post(self, request):
        print('Eliminado post', request.body)
        return HttpResponse(request)
