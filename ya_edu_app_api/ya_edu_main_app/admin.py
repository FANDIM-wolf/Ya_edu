from django.contrib import admin
from .models import User_app, Event ,EventUser,Token_and_User

admin.site.register(User_app)
admin.site.register(Event)
admin.site.register(EventUser)
admin.site.register(Token_and_User)
# Register your models here.
