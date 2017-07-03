from django.contrib import admin
from .models import Imovel

class ImovelAdmin(admin.ModelAdmin):
    model = Imovel
    list_display = ('nome', 'endereco')
    search_fields = ('endereco',)
    actions = None

admin.site.register(Imovel,ImovelAdmin)