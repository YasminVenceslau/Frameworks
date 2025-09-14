from django.http import HttpResponse

# Função da página inicial
def home(request):
    return HttpResponse("<h1>hello world</h1>")
