from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('send-form-email', views.SendFormEmail.as_view(), name='send_mail')
] 