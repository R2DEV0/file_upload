from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Carrier
from django.core.files.storage import FileSystemStorage


# first page of app, login/registration #
def index(request):
    return render(request, 'login.html')


# login existing user created by Admin #
def login(request):
    errors = User.objects.return_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    login_user_list = User.objects.filter(email=request.POST['email'])  
    logged_in_user = login_user_list[0]
    request.session['user_id'] = logged_in_user.id
    return redirect('/dashboard')


# logs in a new user if validations pass #
def new_user(request):
    errors = User.objects.new_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        name= request.POST['name']
        email= request.POST['email']
        password= request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(name=name, home=home, email=email, password=pw_hash)
        request.session['user_id'] = new_user.id
    return redirect('/dashboard')


# main dashboard page #
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'carriers': Carrier.objects.all(),
        'user': user
    }
    return render(request, 'dashboard.html', context)


# add a new carrier to database #
def addNew(request):
    errors = Carrier.objects.carrier_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')
    else:
        num = request.POST['num'] 
        name = request.POST['name']
        packet = request.FILES['packet']
        if not '.pdf' in packet.name:
            raise messages.error(packet, 'Document must be a pdf file')
        else:
            fs = FileSystemStorage()
            fs.save(packet.name, packet)
            new_carrier = Carrier.objects.create(mc_num=num, name=name, packet=packet)
    return redirect('/dashboard')


# view carrier details #
def detail(request, carrier_id):
    if 'user_id' not in request.session:
        return redirect('/') 
    carrier = Carrier.objects.get(id=carrier_id)
    user = User.objects.get(id=request.session['user_id'])
    context={
        'user':user,
        'carrier': carrier
    }
    return render(request, 'detail.html', context)


# Logout user and return to login page #
def logout(request):
    request.session.flush()
    return redirect('/')