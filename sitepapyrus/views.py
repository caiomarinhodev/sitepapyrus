import requests
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
from django.views.generic import TemplateView, FormView

from sitepapyrus.forms import MensagemForm


class IndexView(FormView):
    form_class = MensagemForm
    template_name = 'index.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return super(IndexView, self).get(request, *args, **kwargs)

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


def get_json_insta(request):
    url = 'https://www.instagram.com/papyrusatelie/?__a=1'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/papyrusatelie/?__a=1',
        'cookie': 'ig_did=4745C25C-02D4-425F-9324-E003BAF0DB57; mid=X2T3GQALAAHFyuvWKgtx7E9f9R-H; fbm_124024574287414=base_domain=.instagram.com; shbid=17666; ig_nrcb=1; csrftoken=wa5xb5BjCQ8whqolKLtzaiixxMN98yE8; ds_user_id=2245000297; sessionid=2245000297%3A421nlD49mGYAdR%3A29; shbts=1618835751.7103243; rur=PRN; fbsr_124024574287414=EJY_lL0Rxlep9qk_zL-p8CWaW7GGYguw2RdgtvBkKhQ.eyJ1c2VyX2lkIjoiMTAwMDA0NTMwMTMwODM3IiwiY29kZSI6IkFRQTFsdFpuTmdMcU1COEU2ZU5fVEZON3UwVU9WUXZKMzVtZVprX1JxODJtd2pQaXZzUjVqcDRBRWdHN0pPaHh4RWlpaElvMURNWF9HeGU4VjdMRGU0U2p5bFB6clpwOTc4NnhkZUNTM25MZ1M1U045NTRERFR6U0ZoUjd3dEFmZ2dZS2g5RkdUOHl2UUo5VlBGUnFfLVlQanlYNG53dnhXM0c1eGU0NVVYS0dUQlQtYlFqak9IR21qYUt6UEt4ZmRNY05rQk9iU3NaN1RTZzdwOGtjYnBZNVNPS01GbnZtOXRHVzR0RjVUdnRUWXhmSjZkZVdEVTFMMzM0Z1ZoY0FNT1ZTMm16NWpYLTR5d1Q4Yk9MMkIxOGFkakVoX0MyRk9xUTZHb21KLTdlVVVUR0hCQVNXQ0x6UUZyenlXLXNlR05OaUtSbFpab1FiM2IzMjJZdmJVSTV1Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJ1a3N3UHNnV1hXSUpVV3EycEpldkdlMXlJTkRZOERXNVEzQnJJd1pDclpDeFd0UnVwSjRQVjVZOGhoU01aQWtaQURrUkpRRGpqMTlod0RoMWc1ZGRGaFpCZ0UyUWJJZklSWkJ5NmZBb2x4b1pBOVQ2QW1IWDAweW81MmJZRXdaQXd0c3RKeHRTdzdOa1pDR3VtZWVhcmhrTGN3WTNDdUdhTFRYaHdBYmZSWkNKIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2MTg5MjI3MDl9'
    }
    req = requests.get(url, headers=headers)
    print(req.status_code)
    if req.status_code == 200:
        print(req.text)
        return JsonResponse(req.json())
    else:
        return JsonResponse({})
