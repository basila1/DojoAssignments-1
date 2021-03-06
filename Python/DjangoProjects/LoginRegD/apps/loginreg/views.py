from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    request.session['success'] = False   #  resetting the logged in or registered person
    return render(request, 'loginreg/index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    user = User.objects.register(request.POST)
    if 'errors' in user:
        error = user['errors']
        for one in error:
            messages.error(request, one)
        return redirect('/')
    if user['register'] == True:
        User.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], email = request.POST['email'], password = user['password'])
        user = User.objects.filter(email = request.POST['email'])
        request.session['userid'] = user[0].id
        request.session['success'] = 'registered'
    return redirect('/success')

def success(request):
    if request.session['success'] == False:
        return redirect('/')
    if 'userid' not in request.session:
        return redirect('/')
    context = {'user': User.objects.all(), 'loggeduser': User.objects.filter(id=request.session['userid'])[0]}
    return render(request, 'loginreg/success.html', context)

def login(request):
    if request.method == "GET":
        return redirect('/')
    user = User.objects.login(request.POST)
    if 'errors' in user:
        error = user['errors']
        for one in error:
            messages.error(request, one)
        return redirect('/')
    if user['login'] == True:
        user = User.objects.filter(email = request.POST['email'])
        request.session['userid'] = user[0].id
        request.session['success'] = 'loggedin'
    return redirect('/success')

def delete(request, id):
    if request.method == "GET":
        return redirect('/')
    User.objects.filter(id=id).delete()
    return redirect('/success')

def logout(request):
    if request.method == "GET":
        return redirect('/')
    request.session['success'] = False
    del request.session['userid']
    return redirect('/')
