from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def send_contact_email(request, *args, **kwargs):
    name = kwargs.get("name")
    recipient = kwargs.get("email")
    subject = kwargs.get("subject")
    message = kwargs.get("message")
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
            None,
            f"Une erreur s'est produite lors de l'envoi de votre message : {str(e)}",
        )


def send_volunteer_acceptance_email(request, volunteer):
    subject = "🎉 Félicitations, votre demande de bénévolat a été acceptée !"
    message = f"""
    Bonjour {volunteer.full_name},

    Nous avons le plaisir de vous informer que votre demande de bénévolat au sein de la fondation Arlette Sita été acceptée ! 🎉

    Si vous avez des questions, n’hésitez pas à nous contacter à contact@fondationarlettesita.com.

    À très bientôt !

    L’équipe de la fondation Arlette Sita.
    """

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [volunteer.email],
            fail_silently=False,
        )
    except Exception as e:
        message.error(
            request,
            f"Une erreur s'est produite lors de l'envoi de l'e-mail : {str(e)}",
        )
    else:
        messages.success(
            request,
            "Le bénévole a été accepeter avec succès, l'e-mail de confirmation a été envoyé avec succès au bénévole.",
        )


def send_volunteer_rejection_email(request, volunteer):
    subject = "❌ Désolé, votre demande de bénévolat a été refusée."
    message = f"""
    Bonjour {volunteer.full_name},

    Nous vous remercions d'avoir postulé pour devenir bénévole au sein de la fondation Arlette Sita. Malheureusement, nous ne pouvons pas donner suite à votre candidature pour le moment.

    Nous vous encourageons à rester en contact avec nous et à consulter régulièrement notre site Web pour d'autres opportunités.

    Merci encore pour votre intérêt et votre compréhension.

    À bientôt !

    L’équipe de la fondation Arlette Sita.
    """

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [volunteer.email],
            fail_silently=False,
        )
    except Exception as e:
        messages.error(
            request,
            f"Une erreur s'est produite lors de l'envoi de l'e-mail : {str(e)}",
        )
    else:
        messages.success(
            request,
            "Le bénévole a été refusé avec succès, l'e-mail de confirmation a été envoyé avec succès au bénévole.",
        )
