from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def send_volunteer_acceptance_email(request, volunteer):
    """
    Envoie un e-mail à un bénévole pour l'informer que sa demande a été acceptée.

    Paramètres :
    - volunteer (objet) : instance du bénévole contenant les informations (nom, email, date de début, etc.).
    """
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
