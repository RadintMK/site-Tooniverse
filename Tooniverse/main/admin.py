from django.contrib import admin
from.models import Studio, Cartoon

# Регистрация модели Studio
@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Регистрация модели Cartoon
@admin.register(Cartoon)
class CartoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  
    search_fields = ('title',) 