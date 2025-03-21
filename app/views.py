from django.shortcuts import render

# Create your views here.
def index(request):
    active = 'index'
    return render(request, 'app/index.html', {
        'active': active
    })
    
def about(request):
    active = 'about'
    return render(request, 'app/about.html', {
        'active': active
    })
    
def contact(request):
    active = 'contact'
    return render(request, 'app/contact.html', {
        'active': active
    })