from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student, FriendRequest, FriendList
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from datetime import datetime
from .database import data_posts, data_users
from pinfbetsite.utils import get_friend_request_or_false
from pinfbetsite.friend_request_status import FriendRequestStatus
import json
from .models import Bet
from decimal import *

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
        newStudent = Student(user=newUser)
        newStudent.save()
        newFriendList = FriendList(user=newUser)
        newFriendList.save()
        login(request, newUser)
        return redirect("feed")
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


class Friends(View):
    template = 'friends.html'

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
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def bet_list(request):
    me = request.user
    bets = Bet.objects.filter(student__user = me)
    student = Student.objects.get(user = me)
    if request.method == 'POST':
        actual_grade = request.POST.get('actual_grade')
        bet_grade = request.POST.get('bet_grade')
        bet_coins = request.POST.get('bet_coins')
        pass_rate = request.POST.get('pass_rate')
        bet = Bet.objects.get(id=request.POST.get('bet_id'))
        if actual_grade == bet_grade:
            getcontext().prec = 2
            student.coins += Decimal(bet_coins)/Decimal(pass_rate)
            student.save()
        bet.paid = True
        bet.actual_grade = request.POST.get('actual_grade')
        bet.save()

    return render(request, 'bets.html', {'bets':bets, 'student':student})

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


def account_search_view(request, *args, **kwargs):
    context = {}
    if request.method == "GET":
        search_query = request.GET.get("q")
        if len(search_query) > 0:
            search_results = User.objects.filter(
                username__icontains=search_query).distinct()
            Students = []

            for student in search_results:
                Students.append((student, False))
            context['Students'] = Students

    return render(request, "search_results.html", context)


def account_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = User.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email

        try:
            friend_list = FriendList.objects.get(user=account)
        except FriendList.DoesNotExist:
            friend_list = FriendList(user=account)
            friend_list.save()
        friends = friend_list.friends.all()
        context['friends'] = friends

        is_self = True
        is_friend = False
        request_sent = FriendRequestStatus.NO_REQUEST_SENT.value
        friend_requests = None
        user = request.user

        if user.is_authenticated and user != account:
            is_self = False
            if friends.filter(pk=user.id):
                is_friend = True

            else:
                is_friend = False
                # CASE1: Request has been sent from THEM to YOU: FriendRequestStatus.THEM_SENT_TO_YOU
                if get_friend_request_or_false(sender=account, receiver=user):
                    request_sent = FriendRequestStatus.THEM_SENT_TO_YOU.value
                    context['pending_friend_request_id'] = get_friend_request_or_false(sender=account, receiver=user).id
                # CASE2: Request has been sent from YOU to THEM: FriendRequestStatus.YOU_SENT_TO_THEM
                elif get_friend_request_or_false(sender=user, receiver=account):
                    request_sent = FriendRequestStatus.YOU_SENT_TO_THEM.value
                # CASE3: No request sent from YOU or THEM: FriendRequestStatus.NO_REQUEST_SENT
                else:
                    request_sent = FriendRequestStatus.NO_REQUEST_SENT.value
        elif not user.is_authenticated:
            is_self = False
        else:
            try:
                friend_requests = FriendRequest.objects.filter(receiver=user, is_active=True)
            except:
                pass

            # Set the template variables to the values
        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['request_sent'] = request_sent
        context['friend_requests'] = friend_requests
        context['BASE_URL'] = settings.BASE_URL
        return render(request, "account.html", context)


def friends_list_view(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        user_id = kwargs.get("user_id")
        if user_id:
            try:
                this_user = User.objects.get(pk=user_id)
                context['this_user'] = this_user
            except User.DoesNotExist:
                return HttpResponse("That user does not exist.")
            try:
                friend_list = FriendList.objects.get(user=this_user)
            except FriendList.DoesNotExist:
                return HttpResponse(f"Could not find a friends list for {this_user.username}")

            # Must be friends to view a friends list
            if user != this_user:
                if not user in friend_list.friends.all():
                    return HttpResponse("Tienes que ser amigo para poder ver su lista de amigos.")
            friends = []  # [(friend1, True), (friend2, False), ...]
            # get the authenticated users friend list
            auth_user_friend_list = FriendList.objects.get(user=user)
            for friend in friend_list.friends.all():
                friends.append((friend, auth_user_friend_list.is_mutual_friend(friend)))
            context['friends'] = friends
    else:
        return HttpResponse("Tienes que ser amigo para poder ver su lista de amigos.")
    return render(request, "friends_list.html", context)


def friend_requests(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        user_id = kwargs.get("user_id")
        account = User.objects.get(pk=user_id)
        if account == user:
            friend_requests = FriendRequest.objects.filter(receiver=account, is_active=True)
            context['friend_requests'] = friend_requests
        else:
            return HttpResponse("You can't view another users friend requests.")
    else:
        redirect("login")
    return render(request, "friend_requests.html", context)


def send_friend_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = User.objects.get(pk=user_id)
            try:
                # Get any friend requests (active and not-active)
                friend_requests = FriendRequest.objects.filter(sender=user, receiver=receiver)
                # find if any of them are active (pending)
                try:
                    for request in friend_requests:
                        if request.is_active:
                            raise Exception("You already sent them a friend request.")
                    # If none are active create a new friend request
                    friend_request = FriendRequest(sender=user, receiver=receiver)
                    friend_request.save()
                    payload['response'] = "Friend request sent."
                except Exception as e:
                    payload['response'] = str(e)
            except FriendRequest.DoesNotExist:
                # There are no friend requests so create one.
                friend_request = FriendRequest(sender=user, receiver=receiver)
                friend_request.save()
                payload['response'] = "Friend request sent."

            if payload['response'] == None:
                payload['response'] = "Something went wrong."
        else:
            payload['response'] = "Unable to sent a friend request."
    else:
        payload['response'] = "You must be authenticated to send a friend request."
    return HttpResponse(json.dumps(payload), content_type="application/json")


def accept_friend_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "GET" and user.is_authenticated:
        friend_request_id = kwargs.get("friend_request_id")
        if friend_request_id:
            friend_request = FriendRequest.objects.get(pk=friend_request_id)
            # confirm that is the correct request
            if friend_request.receiver == user:
                if friend_request:
                    # found the request. Now accept it
                    updated_notification = friend_request.accept()
                    payload['response'] = "Friend request accepted."

                else:
                    payload['response'] = "Something went wrong."
            else:
                payload['response'] = "That is not your request to accept."
        else:
            payload['response'] = "Unable to accept that friend request."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to accept a friend request."
    return HttpResponse(json.dumps(payload), content_type="application/json")


def remove_friend(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            try:
                removee = User.objects.get(pk=user_id)
                friend_list = FriendList.objects.get(user=user)
                friend_list.unfriend(removee)
                payload['response'] = "Successfully removed that friend."
            except Exception as e:
                payload['response'] = f"Something went wrong: {str(e)}"
        else:
            payload['response'] = "There was an error. Unable to remove that friend."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to remove a friend."
    return HttpResponse(json.dumps(payload), content_type="application/json")


def decline_friend_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "GET" and user.is_authenticated:
        friend_request_id = kwargs.get("friend_request_id")
        if friend_request_id:
            friend_request = FriendRequest.objects.get(pk=friend_request_id)
            # confirm that is the correct request
            if friend_request.receiver == user:
                if friend_request:
                    # found the request. Now decline it
                    updated_notification = friend_request.decline()
                    payload['response'] = "Friend request declined."
                else:
                    payload['response'] = "Something went wrong."
            else:
                payload['response'] = "That is not your friend request to decline."
        else:
            payload['response'] = "Unable to decline that friend request."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to decline a friend request."
    return HttpResponse(json.dumps(payload), content_type="application/json")


def cancel_friend_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = User.objects.get(pk=user_id)
            try:
                friend_requests = FriendRequest.objects.filter(sender=user, receiver=receiver, is_active=True)
            except FriendRequest.DoesNotExist:
                payload['response'] = "Nothing to cancel. Friend request does not exist."

            # There should only ever be ONE active friend request at any given time. Cancel them all just in case.
            if len(friend_requests) > 1:
                for request in friend_requests:
                    request.cancel()
                payload['response'] = "Friend request canceled."
            else:
                # found the request. Now cancel it
                friend_requests.first().cancel()
                payload['response'] = "Friend request canceled."
        else:
            payload['response'] = "Unable to cancel that friend request."
    else:
        # should never happen
        payload['response'] = "You must be authenticated to cancel a friend request."
    return HttpResponse(json.dumps(payload), content_type="application/json")
