from django.shortcuts import render

# Create your views here.
from django.views import View


class Feed(View):
    template = 'feed.html'

    def get(self, request):
        return render(request, self.template)


class SignUp(View):
    template = 'SignUp.html'

    def get(self, request):
        return render(request, self.template)
class Terms(View):
    template = 'Terms.html'

    def get(self,request):
        return render(request, self.template)