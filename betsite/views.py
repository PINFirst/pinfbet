from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from datetime import datetime
import json


def time_ago_aux(ago, cal):
    return (ago, cal) if ago == 1 else (ago, cal+'s')


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


data = {'posts': [
        {'User': 'Jeff',
         'profile_img': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg',
         'message': 'Me quiero pegar un tiro',
         'type': 'bet',
         'bet': 'Apruebo EDNL con un 7',
         'time': '35 minutes ago',
         'image': None,
         'image_url': None,
         'comments': [
             {'User': 'Sergio',
              'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
              'message': 'Vamos a sacar un diez'
              },
             {'User': 'Sergio',
              'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
              'message': 'Era broma'
              },
             {'User': 'Jeff',
              'profile_img': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg',
              'message': 'Pfff'
              },

         ]
         },
        {'User': 'Maria',
         'profile_img': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg',
         'message': 'Me quiero pegar un tiro x2',
         'type': 'bet',
         'bet': 'Apruebo PINF con un 5',
         'time': '45 minutes ago',
         'image': None,
         'image_url': None,
         'comments': [
             {'User': 'Sergio',
              'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
              'message': 'Vamos a sacar un diez'
              },
             {'User': 'Sergio',
              'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
              'message': 'Era broma'
              },
             {'User': 'Jeff',
              'profile_img': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg',
              'message': 'Pfff'
              },
         ]
         },
        {'User': 'Sergio',
         'profile_img': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg',
         'message': 'Me quiero pegar un tiro x10',
         'type': 'bet',
         'bet': 'Apruebo PCTR con un 10',
         'time': '55 minutes ago',
         'image': None,
         'image_url': None,
         'comments': [
             {'User': 'Sergio',
              'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
              'message': 'Vamos a sacar un diez'
              },
             {'User': 'Sergio',
              'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
              'message': 'Era broma'
              },
             {'User': 'Jeff',
              'profile_img': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg',
              'message': 'Pfff'
              },

         ]
         },
    ]}


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
        global data
        return HttpResponse(json.dumps(data), content_type="application/json")


class SendPost(View):
    def post(self, request):
        global data
        print("Enviado comentario", request)

        user = get_user()

        request_data = json.loads(request.body)

        today = datetime.now()

        time_message = time_ago(today)

        if request_data['type'] == 'bet':
            post = {'User': request_data['user'],
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

            data['posts'].append(post)

            print(data)

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
