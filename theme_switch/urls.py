from django.urls import path, include
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('test', TemplateView.as_view(template_name='test.html'), name='test'),
]
