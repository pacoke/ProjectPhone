from django.shortcuts import render_to_response ,get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render_to_response('index.html')