
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password == password1:
            if User.objects.filter(username=username):
                # messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                # messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                user.save()
                print('User Created')
                return redirect('/')
        else:
            # messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')