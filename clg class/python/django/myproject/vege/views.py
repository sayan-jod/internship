from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate  , login ,logout

# Create your views here.

def receipes(request):
    receipes = Receipe.objects.all()
    return render(request, 'receipes.html', {'receipes': receipes})

def add_receipes(request):
    if request.method == 'POST':
        # Process the uploaded file and save it to the database.
        data = request.POST
        
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')    
        
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
        )
        return redirect('/add_receipes/')
    
    queryset = Receipe.objects.all()
    context = {
       'receipes': queryset,
    }
    
    return render(request, 'add_receipes.html', context)


def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('receipe_image')
        name = data.get('receipe_name')
        description = data.get('receipe_description')    
        
        queryset.receipe_name = name
        queryset.receipe_description = description
        
        if image:
            queryset.receipe_image = image
        
        queryset.save()
        return redirect('/add_receipes/')
        
    
    context = {'receipes': queryset}
    return render(request, 'update_receipe.html', context)


def delete_receipe(request, id):
    receipe = Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('/add_receipes/')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/user_login/')
        
        user = authenticate(username = username , password = password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/user_login/')
        else:
            login(request , user)
            return redirect('/add_receipes/')
        
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return render(request,)

def register_page(request):
    return render(request, 'register.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request,"Username already taken")
            return redirect('/user_register/')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()

        messages.info(request,"Account created succesfully")
        return redirect('/user_register/')   
 
    return render(request, 'register.html')

