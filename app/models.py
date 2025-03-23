from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=False, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    user_type = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "user_type"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username if self.username else self.email


class Event(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, max_length=350)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="events/", blank=True, null=True)
    published = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-publication_date"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
class Volunteer(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'En attente'),
        ('ACCEPTED', 'Accepté'),
        ('REJECTED', 'Rejeté'),
    )
    DISPONIBILITY_CHOICES = (
        ('FULL_TIME', 'Temps plein'),
        ('WEEKEND', 'Weekend'),
    )
    full_name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=10, verbose_name="Téléphone")
    disponibility = models.CharField(max_length=20, choices=DISPONIBILITY_CHOICES, default='FULL_TIME', verbose_name="Disponibilité")
    skill = models.CharField(max_length=100, verbose_name="Compétence")
    motivation = models.TextField(max_length=700, verbose_name="Motivation")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', verbose_name="Statut")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.full_name} ({self.email})"
    
    