from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('create_event/', views.create_event, name='create_event'),
    path('login_user/', views.login_user, name='login_user'),
    path('get_user/<int:user_id>/', views.get_user_by_id, name='get_user_by_id'),
    path('get_user_by_token/', views.get_user_by_token, name='get_user_by_token'),
    path('get_event/<int:event_id>/', views.get_event_by_id, name='get_event_by_id'),
    path('get_closest_events/', views.get_closest_events, name='get_closest_events'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('download_image/<int:event_id>/', views.download_image, name='download_image'),
    path('get_events_for_one_user/<int:user_id>/', views.get_user_events, name='get_user_events'),
    
    # Add more URL patterns for your app here
]

