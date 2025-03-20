from django.shortcuts import render

# Create your views here.
def index(request):
    active = 'index'
    return render(request, 'app/index.html', {
        'active': active
    })