from django.shortcuts import render

# Create your views here.
from django.views import View


class Feed(View):
    template = 'feed/feed.html'

    def get(self, request):
        return render(request, self.template)
