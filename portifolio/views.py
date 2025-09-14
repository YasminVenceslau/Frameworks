from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello word</h1>")
