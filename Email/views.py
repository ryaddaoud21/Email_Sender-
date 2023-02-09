from django.shortcuts import render

# Create your views here.

from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy


class ContactView(FormView):
    template_name = 'Email/Sender.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)



class ContactSuccessView(TemplateView):
    template_name = 'Email/Success.html'