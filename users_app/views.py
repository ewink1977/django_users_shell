from django.shortcuts import render, redirect, HttpResponse

def users_home(request):
    print('This is the USERS HOME page.')
    return HttpResponse('<h1>USERS HOME PAGE!</h1>')


