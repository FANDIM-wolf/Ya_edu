from django.contrib import admin
from .models import User_app, Event ,EventUser

admin.site.register(User_app)
admin.site.register(Event)
admin.site.register(EventUser)

# Register your models here.
