from email import message
# from ssl import _PasswordType
from django.shortcuts import render, redirect
from .models import data
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.
counter = 0


def index(request):
    no_of_words = 0
    no_of_characters = 0
    no_of_sentences = 0
    no_of_paragraph = 0
    counter = 0
    return render(request, 'index.html', {'words': no_of_words, 'char': no_of_characters, 'sentence': no_of_sentences, 'paragraph': no_of_paragraph, 'counter': counter})


def counter(request):
    text = request.GET['text']
    no_of_words = len(text.split())
    no_of_characters = len(text)
    no_of_sentences = len(text.split('.')) - 1
    no_of_paragraph = 0
    # ncount= 0
    for n in text:
        if n == '\n':
            no_of_paragraph += 1

            # ncount += 1
            # if ncount == 2:
            #     no_of_paragraph +=1
            # else:
            #     ncount = 0
    if no_of_paragraph == 0:
        no_of_paragraph = 1

    # free trial
    if request.user.is_authenticated:
        counter = 0
    else:
        counter = 1

    # updating database

    if request.user.is_authenticated:
        username = request.user.username
        user = request.user

        username = data()
        username.email = user.email
        username.text = text
        username.words = no_of_words
        username.characters = no_of_characters
        username.sentences = no_of_sentences
        username.paragraphs = no_of_paragraph
        username.save()

    return render(request, 'index.html', {'words': no_of_words, 'char': no_of_characters, 'sentence': no_of_sentences, 'paragraph': no_of_paragraph, 'counter': counter, 'text':text})


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            message.info(request, 'Email already exists.')
            return redirect('signup')
        else:
            user = User.objects.create_user(
                username=name, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            message.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'signin.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def history(request):
    datalist = data.objects.all()
    user = request.user
    return render(request, 'history.html', {'data': datalist, 'user': user})

def admin(request):
    users = User.objects.all()
    userData = data.objects.all()
    return render(request, 'admin/panel.html', {'users':users, 'data':userData})


def delete(request):
    id = request.GET['id']
    record = data.objects.get(id = id)
    
    record.delete()
    
    users = User.objects.all()
    userData = data.objects.all()
    return render(request, 'admin/panel.html', {'users':users, 'data':userData})

def add(request):
    name = request.GET['name']
    email = request.GET['email']
    password = request.GET['password']

    if User.objects.filter(email=email).exists():
        message.info(request, 'Email already exists.')
    else:
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()

    users = User.objects.all()
    userData = data.objects.all()
    return render(request, 'admin/panel.html', {'users':users, 'data':userData})


def deleteUser(request):
    email = request.GET['email']
    record = User.objects.get(email = email)
    record.delete()

    users = User.objects.all()
    userData = data.objects.all()
    return render(request, 'admin/panel.html', {'users':users, 'data':userData})


    
