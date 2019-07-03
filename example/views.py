from django.shortcuts import render
from example.forms import UserForm,UserProfileInfoForm, ObjectForm
from django.views.decorators.cache import cache_page
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from example.models import Object

def index(request):
    return render(request,'example/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'example/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                request.session['username'] = username
                request.session.set_expiry(8640)
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'example/login.html', {})

@login_required
def add_object(request):
    registered = False
    if request.method == 'POST':
        object_form = ObjectForm(data=request.POST)
        if object_form.is_valid():
            print(object_form)
            object = object_form.save(commit=False)
            object.user = request.user
            object.save()
            registered = True
            request.session.set_expiry(864)
        else:
            print(object_form.errors)
    else:
        object_form = ObjectForm()
    return render(request,'example/add_object.html',
                          {'object_form':object_form, 'registered': registered,
                          'objects': Object.objects.all().filter(user=request.user)})
