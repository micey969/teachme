from django.urls import path
from django.views.generic import TemplateView


app_name = 'services'

urlpatterns = [
    path('termsofuse',TemplateView.as_view(template_name="services/terms.html"),name='terms'),
    path('privacy',TemplateView.as_view(template_name="services/privacy.html"),name='privacy'),
    path('faqs',TemplateView.as_view(template_name="services/faqs.html"),name='faqs'),
    path('about',TemplateView.as_view(template_name="services/about.html"),name='about'),

]
