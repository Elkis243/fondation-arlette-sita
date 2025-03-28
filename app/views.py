from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import *
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

MAX_IMAGE_SIZE = 1 * 1024 * 1024


def index(request):
    active = "index"
    latest_events = Event.objects.all()[:2]
    return render(request, "app/index.html", {"active": active, 'latest_events': latest_events})


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
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        disponibility = request.POST.get("disponibility")
        skill = request.POST.get("skill")
        motivation = request.POST.get("motivation")
        status = "PENDING"
        volunteer = Volunteer(
            full_name=full_name,
            email=email,
            phone=phone,
            disponibility=disponibility,
            skill=skill,
            motivation=motivation,
            status=status,
        )
        volunteer.save()
        messages.success(
            request,
            "Votre demande de bénévolat a été enregistrée avec succès. Nous vous contacterons bientôt !",
        )
        return HttpResponseRedirect("/add-volunteer/")
    return render(request, "app/add_volunteer.html")


@login_required
def list_volunteer(request):
    active = "volunteer"
    all_volunteers = Volunteer.objects.all().order_by("-created_at")
    return render(
        request,
        "app/list_volunteer.html",
        {"active": active, "all_volunteers": all_volunteers},
    )


@login_required
def detail_volunteer(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    active = "volunteer"
    return render(
        request, "app/detail_volunteer.html", {"active": active, "volunteer": volunteer}
    )

@login_required
def dimmiss_volunteer(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    volunteer.delete()
    messages.success(request, "Le bénévole a été rejeté avec succès.")
    return redirect("list_volunteer")

@login_required
def accept_volunteer(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    volunteer.status = "ACCEPTED"
    volunteer.save()
    messages.success(request, "Le bénévole a été accepeter avec succès.")
    return redirect("list_volunteer")


def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.user_type == 'admin':
                login(request, user)
                return redirect("faspanel")
            else:
                messages.error(request, "Vous n'avez pas accès à cette page !")
                return redirect("signin")
        else:
            messages.error(request, "Identifiants invalides. Veuillez réessayer !")
            return redirect("signin")
    return render(request, "app/signin.html")


def disconnection(request):
    logout(request)
    return redirect("index")

@login_required
def faspanel(request):
    active = "dashboard"
    total_event = Event.objects.filter(published=True).count()
    total_request_volunteer = Volunteer.objects.filter(status="PENDING").count()
    total_volunteer = Volunteer.objects.filter(status="ACCEPTED").count()
    latest_volunteers = Volunteer.objects.filter(status="PENDING").order_by(
        "-created_at"
    )[:3]
    latest_events = Event.objects.filter(published=True).order_by("-publication_date")[:3]
    return render(
        request,
        "app/dashboard.html",
        {
            "active": active,
            "latest_volunteers": latest_volunteers,
            "total_volunteer": total_volunteer,
            "total_request_volunteer": total_request_volunteer,
            "latest_events": latest_events,
            "total_event": total_event,
        },
    )


def add_news(request):
    active = "add_news"
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        slug = slugify(title)

        if Event.objects.filter(slug=slug).exists():
            messages.error(
                request, "Le slug est déjà utilisé. Veuillez choisir un autre titre !"
            )
            return redirect("add_news")

        if image:
            if isinstance(image, InMemoryUploadedFile) and image.size > MAX_IMAGE_SIZE:
                messages.error(
                    request,
                    "L'image est trop lourde ! Taille maximale autorisée : 5 Mo !",
                )
                return redirect("add_news")

        Event.objects.create(
            title=title,
            description=content,
            image=image,
            published=True,
            user=request.user,
            slug=slug,
        )
        messages.success(request, "Événement ajouté avec succès !")
        return redirect("add_news")

    return render(request, "app/add_news.html", {"active": active})

@login_required
def list_news(request):
    active = "add_news"
    events = Event.objects.filter(published=True).order_by("-publication_date")
    return render(request, "app/list_news.html", {"active": active, "events": events})

@login_required
def news_delete(request, slug):
    event = get_object_or_404(Event, slug=slug)
    event.delete()
    messages.success(request, "Événement supprimé avec succès.")
    return redirect("list_news")

@login_required
def news_edit(request, slug):
    active = "add_news"
    event = get_object_or_404(Event, slug=slug)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        if image:
            if isinstance(image, InMemoryUploadedFile) and image.size > MAX_IMAGE_SIZE:
                messages.error(
                    request,
                    "L'image est trop lourde ! Taille maximale autorisée : 5 Mo !",
                )
                return redirect("edit_news", slug=slug)

        event.title = title
        event.description = content
        if image:
            event.image = image
        event.save()
        messages.success(request, "Événement modifié avec succès !")
        return redirect("list_news")
    return render(request, "app/edit_news.html", {"active":active, "event": event})

def news_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, "app/detail_news.html", {"event": event, 'object_or_url': request.build_absolute_uri()})

def blog(request):
    active = "blog"
    events = Event.objects.filter(published=True).order_by("-publication_date")
    paginator = Paginator(events, 6)

    page_number = request.GET.get("page")
    events = paginator.get_page(page_number)

    return render(
        request, "app/blog.html", {"events": events, "active": active}
    )

@login_required
def profile(request):
    active = "profile"
    return render(request, "app/profile.html", {"active": active})
