from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

