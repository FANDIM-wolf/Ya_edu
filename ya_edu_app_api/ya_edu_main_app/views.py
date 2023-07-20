import datetime
from django.shortcuts import render
from .models import *
from django.http import JsonResponse, FileResponse , HttpResponseGone , HttpResponseNotFound , HttpResponse
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
import jsonpickle
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken

def authenticate_user(login ,password):
    Users = User_app.objects.all()
    for user in Users:
        if user.login == login and user.password == password:
            return True
    return False

@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        type = request.POST.get('type')
        name = request.POST.get('name')
        region = request.POST.get('region')
        city = request.POST.get('city')
        date_of_birth = request.POST.get('date_of_birth')
        login = request.POST.get('login')
        password = request.POST.get('password')
        field_of_study = request.POST.get('field_of_study')
        phone_of_user = request.POST.get('phone_of_user')
        email_of_user = request.POST.get('email_of_user')

        # Create a new User_app object and assign the data
        user = User_app(
            type=type,
            name=name,
            region=region,
            city=city,
            date_of_birth=date_of_birth,
            login=login,
            password=password,
            field_of_study=field_of_study,
            phone_of_user=phone_of_user,
            email_of_user=email_of_user
        )

        # Save the User_app object to the database
        user.save()

        return HttpResponse('User created successfully.')
    else:
        return HttpResponse('Invalid request method.')
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        status = request.POST.get('status')
        status_exist = request.POST.get('status_exist')
        amount_of_clients_at_event = request.POST.get('amount_of_clients_at_event')
        phone_of_admin = request.POST.get('phone_of_admin')
        location = request.POST.get('location')
        date_of_start_request = request.POST.get('date_of_start_request')
        date_of_end_request = request.POST.get('date_of_end_request')
        date_begin = request.POST.get('date_begin')
        date_end = request.POST.get('date_end')
        theme =request.POST.get('theme')
        type = request.POST.get('type')

        # Create a new Event object and assign the data
        event = Event(
            name=name,
            status=status,
            status_exist=status_exist,
            amount_of_clients_at_event=amount_of_clients_at_event,
            phone_of_admin=phone_of_admin,
            location=location,
            date_of_start_request=date_of_start_request,
            date_of_end_request=date_of_end_request,
            date_begin=date_begin,
            date_end=date_end,
            theme = theme,
            type = type

        )

        # Save the Event object to the database
        event.save()

        return HttpResponse('Event created successfully.')
    else:
        return HttpResponse('Invalid request method.')
@csrf_exempt
@api_view(['GET'])
def get_user_by_id(request, user_id):
    try:
        # Retrieve the user object from the database using the user_id
        user = User_app.objects.get(id=user_id)

        # Create a dictionary of the user's data
        user_data = {
            'id': user.id,
            'type': user.type,
            'name': user.name,
            'region': user.region,
            'city': user.city,
            'date_of_birth': user.date_of_birth,
            'login': user.login,
            'password': user.password,
            'field_of_study': user.field_of_study,
            'phone_of_user': user.phone_of_user,
            'email_of_user': user.email_of_user,
            # Add more fields as needed
        }

        # Return the user data as a JSON response
        return JsonResponse(user_data)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found.'})

@csrf_exempt
@api_view(['GET'])
def get_event_by_id(request, event_id):
    try:
        # Retrieve the event object from the database using the event_id
        event = Event.objects.get(id=event_id)

        # Create a dictionary of the event's data
        event_data = {
            'id': event.id,
            'name': event.name,
            'status': event.status,
            'status_exist': event.status_exist,
            'amount_of_clients_at_event': event.amount_of_clients_at_event,
            'phone_of_admin': event.phone_of_admin,
            'location': event.location,
            'date_of_start_request': event.date_of_start_request,
            'date_of_end_request': event.date_of_end_request,
            'date_begin': event.date_begin,
            'date_end': event.date_end,
            # Add more fields as needed
        }

        # Return the event data as a JSON response
        return JsonResponse(event_data)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Event not found.'})
    
def get_all_events(request):
    # Retrieve all the event objects from the database
    events = Event.objects.all()

    # Create a list of dictionaries containing the data for each event
    event_list = []
    for event in events:
        event_data = {
            'id': event.id,
            'name': event.name,
            'status': event.status,
            'status_exist': event.status_exist,
            'amount_of_users': event.amount_of_users,
            'phone_of_admin': event.phone_of_admin,
            'location': event.location,
            'date_of_start_request': event.date_of_start_request,
            'date_of_end_request': event.date_of_end_request,
            'date_begin': event.date_begin,
            'date_end': event.date_end,
            # Add more fields as needed
        }
        event_list.append(event_data)

    # Return the list of events as a JSON response
    return JsonResponse(event_list, safe=False)

@csrf_exempt
@api_view(['GET'])
def get_user_events(request, user_id):
    try:
        # Retrieve the EventUser object from the database using the user_id
        events_user = list(EventUser.objects.filter(user_id=user_id))
        objects_to_predict = []
        array_of_user_events = [] # events where user was
        for event in events_user:
            event_user = Event.objects.get(id=event.event.id)
            # Serialize the Event object using jsonpickle
            event_json = jsonpickle.encode(event_user)
            array_of_user_events.append(event_json)
        for event in events_user:
            if(event.status == "ds"):
                event_user = event
                event_json = jsonpickle.encode(event_user)
                objects_to_predict.append(event_json)
        common_array = []
        common_array.append(array_of_user_events)
        common_array.append(objects_to_predict)

        
       
                
    

        # Return the list of events as a JSON response
        return JsonResponse(common_array , safe=False)
    except User_app.DoesNotExist:
        return JsonResponse({'error': 'User not found.'})

@csrf_exempt
@api_view(['POST'])
def login_user(request):
    login  = request.POST.get('login')
    password = request.POST.get('password')
    check_authentication = authenticate_user(login,password)
    if check_authentication == True:
        user = User_app.objects.get(login = login)
        tokens= Token_and_User.objects.all()
        
        access_token = AccessToken.for_user(user)
        if access_token  in tokens:
            Token_and_User.objects.filter(token=access_token).delete()
            #save information about token 
            token_and_user = Token_and_User(
                user_id = user,
                token =access_token
            )
            token_and_user.save()
        else:
            #save information about token 
            token_and_user = Token_and_User(
                user_id = user,
                token =access_token
            )
            token_and_user.save()
        # make access_token JsonSizeable
        access_token = jsonpickle.encode(access_token) 
        return JsonResponse({
            "token":access_token,
            "message":"success"
        })
    else :
        return JsonResponse({'error': 'User not found.'})
@csrf_exempt
@api_view(['POST'])
def get_user_by_token(request):
    try:
        token = request.POST.get('token')
        token_to_find_user = Token_and_User.objects.get(token=token)
        # Retrieve the user object from the database using the user_id
        user = User_app.objects.get(id=token_to_find_user.user_id.id)
        
        # Create a dictionary of the user's data
        user_data = {
            'id': user.id,
            'type': user.type,
            'name': user.name,
            'region': user.region,
            'city': user.city,
            'date_of_birth': user.date_of_birth,
            'login': user.login,
            'password': user.password,
            'field_of_study': user.field_of_study,
            'phone_of_user': user.phone_of_user,
            'email_of_user': user.email_of_user,
            # Add more fields as needed
        }

        # Return the user data as a JSON response
        return JsonResponse(user_data)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found.'})