from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from.views import *

urlpatterns = [
     path('', main_page, name='home'),
     path('create', create_page, name='create'),
     path('studios', studios_page, name='studios'),
     path('cartoon', cartoon_page, name='cartoon'),
     path("register", register_request, name="register"),
     path("login", login_request, name="login"),
     path("logout", logout_request, name= "logout"),
     path('send_message/', send_message, name='send_message'),
     path('get_messages/', get_messages, name='get_messages'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
