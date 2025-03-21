from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt  # Add this for CSRF exemption

# Members view
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

# Index view
def index(request):
    return HttpResponse("Welcome to the index page!")

# Login view
@csrf_exempt  # Exempt this view from CSRF verification
def login_view(request):
    if request.method == 'POST':
        # Use request.POST for form data or request.body for JSON data
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    return JsonResponse({'message': 'Invalid request method'}, status=405)