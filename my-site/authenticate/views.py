from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

def home(request):
 	return render(request, 'authenticate/home.html', {})

def login_user (request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You have been logged in') )
			return redirect('home')
		else:
			messages.success(request, ('Error logging in - Please Try Again') )
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('You have been logged out !!') )
	return redirect('home')

def register_user(request):
	if request.method == 'post':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(rquest, user)
			messages.success(request, ('You have been registered !!') )
			return redirect('home')


	else:
		form = SignUpForm()	

	content = {'form': form}
	return render(request, 'authenticate/register.html', content)
 