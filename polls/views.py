from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Students
import datetime
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def hello(request):
    return HttpResponse("Hello, 你现在在hello函数里面")
def getStudent(request):
    listStudents = Students.objects.order_by('signup_date')
    now = datetime.datetime.now()
    out = ","+str(now)+","
    out=out.join([p.name for p in listStudents])
    return HttpResponse(out)