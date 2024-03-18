from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Doctor,Person
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        failed_attempts = request.session.get('failed_attempts', 0)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['failed_attempts'] = 0
            login(request, user)

            success_logins = request.COOKIES.get('success_logins', 0)
            success_logins = int(success_logins) + 1

            response = redirect('list_items')
            response.set_cookie('success_logins', success_logins)
            return response
        else:
            failed_attempts += 1
            request.session['failed_attempts'] = failed_attempts
            if failed_attempts >= 3:
                messages.error(request, 'You have reached maximum login attempts. Please try again later.')
                return redirect('login')
            else:
                return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def list_items(request):
    doctors = Doctor.objects.all()
    return render(request, 'list_items.html', {'doctors': doctors})

def adduser(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname=request.POST['lastname']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        place = request.POST['place']
        password = request.POST['password']

        user_instance = User(username=username, first_name=firstname,last_name=lastname, email=email)
        user_instance.set_password(password)
        user_instance.save()

        user = Person(username=username, firstname=firstname,lastname=lastname, gender=gender, phone=phone, email=email, place=place)
        user.save()
        return HttpResponse('Successfully added')
    return render(request, 'adduser.html')