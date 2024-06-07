from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def main_page(request):
    return render(request, 'main/home.html')

def create_page(request):
    return render(request, 'main/create.html')

def studios_page(request):
    return render(request, 'main/studios.html')

def cartoon_page(request):
    return render(request, 'main/cartoon.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Регистрация успешна." )
			return redirect("home")
		messages.error(request, "Неудачная регистрация. Не верная информация.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Вы вошли как пользователь {username}.")
				return redirect("home")
			else:
				messages.error(request,"Неверный Логин или Пароль")
		else:
			messages.error(request,"Неверный Логин или Пароль")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")