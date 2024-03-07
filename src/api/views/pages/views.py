from django.conf import settings
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = str(settings.REACT_BASE_TEMPLATE)


class AboutView(TemplateView):
    template_name = "about.html"
