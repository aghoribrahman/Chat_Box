from django.contrib import admin
from .models import ChatRoom ,Message
# Register your models here.


@admin.register(ChatRoom)
class Query_model_admin(admin.ModelAdmin):
    list_display =["name"]


@admin.register(Message)
class Query_model_admin(admin.ModelAdmin):
    list_display =["chatroom","sender","message","timestamp"]
