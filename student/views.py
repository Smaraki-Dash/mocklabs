from django.shortcuts import render
from student.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from HR.models import *

# Create your views here.

def login_required(func):
    def inner(request,*args, **kwargs):
        un=request.session.get('username')
        if un:
            print(un)
            return func(request, *args,**kwargs)
        return HttpResponseRedirect(reverse('student_login'))
    return inner


def student_home(request):
    return render(request,'student/student_home.html')

def student_register(request):
    ESUFO=StudentUserForm()
    ESPFO=StudentProfileForm()
    d={'ESUFO':ESUFO, 'ESPFO':ESPFO}
    if request.method == 'POST' and request.FILES:
        SUFDO=StudentUserForm(request.POST)
        SPFDO=StudentProfileForm(request.POST, request.FILES)
        if SUFDO.is_valid() and SPFDO.is_valid():
            pw=SUFDO.cleaned_data.get('password')
            MSUFDO=SUFDO.save(commit=False)
            MSUFDO.set_password(pw)
            MSUFDO.save()
            MSPFDO=SPFDO.save(commit=False)
            MSPFDO.username=MSUFDO
            MSPFDO.save()
            return HttpResponseRedirect(reverse('student_login'))
        return HttpResponse('Invalid data')
    return render(request, 'student/student_register.html',d)

def student_login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        AUO=authenticate(username=un, password=pw)
        if AUO:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('student_home'))
        return HttpResponse('Invalid Credentials')
    return render(request, 'student/student_login.html')

@login_required
def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('student_home'))

@login_required
def mock_ratings(request):
    all_ratings=Ratings.objects.all()
    d={'all_ratings' : all_ratings}
    return render(request, 'student/mock_ratings.html',d)