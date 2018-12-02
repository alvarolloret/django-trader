from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class LoggedPage(TemplateView):
    template_name = 'logged.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class IndexPage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("logged"))
        return super().get(request, *args, **kwargs)
