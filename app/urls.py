from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    # Vue pour demander la réinitialisation
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="password_reset"),
    
    # Vue après l'envoi du lien
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    
    # Vue pour entrer un nouveau mot de passe
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    
    # Vue après succès de la réinitialisation
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
    path("faspanel/", views.faspanel, name="faspanel"),
    path("blog/", views.blog, name="blog"),
    path("add-news/", views.add_news, name="add_news"),
    path("list-news/", views.list_news, name="list_news"),
    path("news-delete/<slug:slug>/", views.news_delete, name="news_delete"),
    path("news-edit/<slug:slug>/", views.news_edit, name="news_edit"),
    path("news-detail/<slug:slug>/", views.news_detail, name="news_detail"),
]
