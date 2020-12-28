from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import json

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
        print("Enviado comentario", request)

        user = get_user()
        #
        data = json_data = json.loads(request.body)

        print(data)

        # post = {'User': user['name'],
        #  'profile_img': user['profile_img'],
        #  'message': 'Me quiero pegar un tiro',
        #  'type': 'bet',
        #  'bet': 'Apruebo EDNL con un 7',
        #  'time': '35 minutes ago',
        #  'image': None,
        #  'image_url': None,
        #  'comments': [
        #      {'User': 'Sergio',
        #       'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
        #       'message': 'Vamos a sacar un diez'
        #       },
        #      {'User': 'Sergio',
        #       'profile_img': 'https://images.pexels.com/photos/1998456/pexels-photo-1998456.jpeg',
        #       'message': 'Era broma'
        #       },
        #      {'User': 'Jeff',
        #       'profile_img': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg',
        #       'message': 'Pfff'
        #       },
        #
        #  ]
        #  }

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
