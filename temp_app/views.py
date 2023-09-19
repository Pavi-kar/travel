from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Team

# Create your views here.
def home(request):
    obj = Place.objects.all()
    per = Team.objects.all()

    return render(request,"index.html",{'display':obj,'members':per})