
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main import  views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about-us/', TemplateView.as_view(template_name='about_us.html'), name='about'),
    path('contact_us/', views.ContactUsView.as_view(), name="contact_us"),
]
