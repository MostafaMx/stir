from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Person, Meetingtime, Service, Question
from django.contrib.auth.decorators import login_required
from random import randint

def home(request):
    return render(request, 'index.html')
# Create your views here.
def sign_in(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_url')
            messages.success(request, 'Logged in successfully.')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('sign_in_url')    
    return render(request, 'sign-in.html') 
        
    
def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if not (name or email or password):
            messages.error(request, 'Please fill out all fields.')
            return redirect('sign_up_url')
        elif Person.objects.filter(username=name).exists() or Person.objects.filter(email=email).exists():
            messages.error(request, 'Username already exists.')
            return redirect('sign_up_url')
        else:
            user = Person.objects.create_user(username=name, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('home_url')
    return render(request, 'sign-up.html')

@login_required
def meetingtime_view(request):
    if request.method == 'POST':
        name = request.POST.get('randomname', '')
        email = request.POST.get('randomemail', '')
        favouraite = request.POST.get('favouraite', '')
        budget = request.POST.get('budget', '')
        message = request.POST.get('message', '')

        if not (name and email and favouraite and budget and message):
            messages.error(request, 'Please fill out all fields.')
            return redirect('home_url')

        meetingtime = Meetingtime.objects.create(
            user=request.user if request.user.is_authenticated else None,
            name=name,
            email=email,
            favouraite=favouraite,
            budget=budget,
            message=message
        )
        messages.success(request, 'Your meeting time has been scheduled successfully.')
        print("Meetingtime created:", meetingtime)
        return redirect('home_url')

    return render(request, 'index.html')

def service_detail(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return HttpResponse("Service not found", status=404)
    return render(request, 'service-details.html', {'service': service})


def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

from django.shortcuts import render, get_object_or_404

# ...

def faq(request):
    questions = Question.objects.all()
    return render(request, 'faq.html', {'questions': questions})
