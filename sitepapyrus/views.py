from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from sitepapyrus.forms import MensagemForm


class IndexView(FormView):
    form_class = MensagemForm
    template_name = 'index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        return super(IndexView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Mensagem enviada com sucesso.')
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar a mensagem, tente novamente.')
        return super(IndexView, self).form_invalid(form)


class EbookPage(TemplateView):
    template_name = 'ebook_page.html'

