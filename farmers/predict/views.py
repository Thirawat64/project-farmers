from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import *


# Create your views here.
def index(req):
    return render(req, 'predict/index.html')