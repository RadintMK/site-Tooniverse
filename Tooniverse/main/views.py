from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from.models import *

def main_page(request):
    return render(request, 'main/home.html')

def create_page(request):
    return render(request, 'main/create.html')

def studios_page(request):
    studios = Studio.objects.all()
    return render(request, 'main/studios.html', {'studios': studios})

def cartoon_page(request):
    cartoons = Cartoon.objects.all()
    return render(request, 'main/cartoon.html', {'cartoons': cartoons})


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


def send_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        Message.objects.create(author=request.user.username, content=message_content)
        return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def get_messages(request):
    since_id = int(request.GET.get('since', 0))
    messages = Message.objects.filter(id__gt=since_id).order_by('-timestamp')[:10]
    messages_data = [{'id': m.id, 'content': m.content, 'author': m.author} for m in messages]
    return JsonResponse(messages_data, safe=False)