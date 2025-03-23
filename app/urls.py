from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("add_volunteer/", views.add_volunteer, name="add_volunteer"),
    path("list_volunteer/", views.list_volunteer, name="list_volunteer"),
    path("detail_volunteer/", views.detail_volunteer, name="detail_volunteer"),
    path("signin/", views.signin, name="signin"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
    path("faspanel/", views.faspanel, name="faspanel"),
    path("add_news/", views.add_news, name="add_news"),
    path("list_news/", views.list_news, name="list_news"),
]
