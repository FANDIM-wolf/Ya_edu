from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('create_event/', views.create_event, name='create_event'),
    path('get_user/<int:user_id>/', views.get_user_by_id, name='get_user_by_id'),
    path('get_event/<int:event_id>/', views.get_event_by_id, name='get_event_by_id'),
    # Add more URL patterns for your app here
]

