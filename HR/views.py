from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from manager.models import *
from manager.forms import *

# Create your views here.
def hr_home(request):
    return render(request, 'hr/hr_home.html')

def hr_login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        AUO=authenticate(username=un, password=pw)
        if AUO.is_active and AUO.is_staff:
            emp_profile=EmployeeProfile.objects.get(username=AUO)
            print(emp_profile.role)
            if emp_profile.role == 'HR':
                login(request, AUO)
                request.session['hruser'] = un
                return HttpResponseRedirect(reverse('hr_home'))
            return HttpResponse("can't login you are not a HR")
        return HttpResponse('Invalid User')
    return render(request, 'hr/hr_login.html')

def hr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hr_home'))


