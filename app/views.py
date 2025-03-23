from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect


def index(request):
    active = "index"
    return render(request, "app/index.html", {"active": active})

def about(request):
    active = "about"
    return render(request, "app/about.html", {"active": active})

def contact(request):
    active = "contact"
    if request.method == "POST":
        name = request.POST.get("name")
        recipient = request.POST.get("email")
        subject = request.POST.get("objet")
        message = request.POST.get("message")
        sender = settings.EMAIL_HOST_USER
        try:
            send_mail(
                subject=f"Message de {name} - {subject}",
                message=message,
                from_email=sender,
                recipient_list=[recipient],
                fail_silently=False,
            )
            messages.success(
                request,
                "Votre message a été envoyé avec succès. Nous vous répondrons bientôt !",
            )
        except Exception as e:
            messages.error(
                request,
                f"Une erreur s'est produite lors de l'envoi de votre message : {str(e)}",
            )

        return HttpResponseRedirect("/contact/")
    return render(request, "app/contact.html", {"active": active})

def add_volunteer(request):
    return render(request, "app/add_volunteer.html")

def list_volunteer(request):
    active = "volunteer"
    return render(request, "app/list_volunteer.html", {'active': active})

def detail_volunteer(request):
    active = "volunteer"
    return render(request, "app/detail_volunteer.html", {'active': active})

def signin(request):
    return render(request, "app/signin.html")

def logout(request):
    return redirect('index')

def faspanel(request):
    active = "dashboard"
    return render(request, "app/dashboard.html", {'active': active})

def add_news(request):
    active = 'add_news'
    return render(request, "app/add_news.html", {'active': active})

def list_news(request):
    active = 'add_news'
    return render(request, "app/list_news.html", {'active': active})

def profile(request):
    active = 'profile'
    return render(request, "app/profile.html", {'active': active})
