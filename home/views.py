from django.shortcuts import render
from jobs.models import *

# Create your views here.
def home(request):
   job = Job.objects.all()
   context = {'job':job}
   # response = requests.get(http://127.0.0.1:8000/api/jobs)
   return render(request, 'home.html',context)
def lists(request):
   # response = requests.get(http://127.0.0.1:8000/api/jobs)
    job = Job.objects.all()
    context = {'job':job}
    return render(request, "list.html", context)