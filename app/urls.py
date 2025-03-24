from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("add-volunteer/", views.add_volunteer, name="add_volunteer"),
    path("list-volunteer/", views.list_volunteer, name="list_volunteer"),
    path("detail-volunteer/<int:pk>/", views.detail_volunteer, name="detail_volunteer"),
    path("dismiss-volunteer/<int:pk>/", views.dimmiss_volunteer, name="dismiss_volunteer"),
    path("accept-volunteer/<int:pk>/", views.accept_volunteer, name="accept_volunteer"),
    path("signin/", views.signin, name="signin"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.disconnection, name="logout"),
    path("faspanel/", views.faspanel, name="faspanel"),
    path("blog/", views.blog, name="blog"),
    path("add-news/", views.add_news, name="add_news"),
    path("list-news/", views.list_news, name="list_news"),
    path("news-delete/<slug:slug>/", views.news_delete, name="news_delete"),
    path("news-edit/<slug:slug>/", views.news_edit, name="news_edit"),
    path("news-detail/<slug:slug>/", views.news_detail, name="news_detail"),
]
