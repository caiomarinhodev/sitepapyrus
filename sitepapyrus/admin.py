from django.contrib import admin

# Register your models here.
from sitepapyrus.models import Item, Mensagem


class ItemAdmin(admin.ModelAdmin):
    search_fields = (
        'titulo', 'descricao'
    )
    list_display = ('id', 'titulo', 'descricao', 'foto_url', 'created_at')


class MensagemAdmin(admin.ModelAdmin):
    search_fields = (
        'nome', 'email', 'whatsapp'
    )
    list_display = ('nome', 'id', 'email', 'whatsapp', 'created_at')


admin.site.register(Item, ItemAdmin)
admin.site.register(Mensagem, MensagemAdmin)
