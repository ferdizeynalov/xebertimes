from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from news.models import News
from .models import Partners
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

'''
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'page-contact.html')
'''


def IndexView(request):
    num_visits = 0
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits': num_visits,
               'newses': News.objects.filter(available=True).order_by('-date')[:6],
               'total_news': News.objects.filter(available=True).count(),
               'partners': Partners.objects.all()[:2],
               }
    return render(request, 'index.html', context=context)


class ContactView(SuccessMessageMixin,FormView):
    template_name = 'page-contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Mesajiniz ugurla gonderildi'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


