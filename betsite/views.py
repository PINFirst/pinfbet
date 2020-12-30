from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
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


def get_user():
    user = {}
    user['name'] = 'Jeff'
    user['profile_img'] = 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg'
    return user


class Feed(View):
    template = 'feed/feed.html'

    def get(self, request):
        return render(request, self.template)


class GetPosts(View):
    def get(self, request):
        return HttpResponse(json.dumps(data_posts), content_type="application/json")


class SendPost(View):
    def post(self, request):
        print("Enviado comentario", request)

        user = get_user()
        owner = 1

        request_data = json.loads(request.body)

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
                'time': time_message,
                'image': None,
                'image_url': None,
                'comments': [
                ]
            }

            data_posts['posts'].append(post)

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
