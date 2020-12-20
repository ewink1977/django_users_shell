from django.shortcuts import render, redirect, HttpResponse
from .models import Users

def users_home(request):
    print('This is the USERS HOME page.')
    context = {
        "users_list": Users.objects.all(),
    }
    return render(request, 'users/index.html', context)

def users_add(request):
    newfirst_name = request.POST['first_name']
    newlast_name = request.POST['last_name']
    newemail = request.POST['email']
    newage = request.POST['age']
    Users.objects.create(first_name=newfirst_name, last_name=newlast_name, email_address=newemail, age=newage)
    return redirect(users_home)
