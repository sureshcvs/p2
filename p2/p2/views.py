from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("welcome To My world")