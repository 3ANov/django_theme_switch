from django.urls import path

from theme_switch.views import HomePageTemplateView, TestPageTemplateView

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home'),
    path('test', TestPageTemplateView.as_view(), name='test'),
]
