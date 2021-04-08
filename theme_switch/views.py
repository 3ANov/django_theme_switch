from django.views import View
from django.views.generic import TemplateView
import json


class LightDarkSwitchView(View):
    def post(self, request, *args, **kwargs):
        post_data = json.loads(request.body.decode("utf-8"))
        request.session['dark_theme_flag'] = post_data['dark_theme_flag']
        return self.get(request, *args, **kwargs)


class HomePageTemplateView(TemplateView, LightDarkSwitchView):
    template_name = 'home.html'


class TestPageTemplateView(TemplateView, LightDarkSwitchView):
    template_name = 'test.html'
