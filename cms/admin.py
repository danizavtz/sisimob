from django.contrib import admin
from .models import Imovel

class ImovelAdmin(admin.ModelAdmin):
    model = Imovel
    list_display = ('nome', 'endereco', 'image_tag')
    search_fields = ('endereco',)
    list_display_links = None
    actions = None
    readonly_fields = ('image_tag',)
	
    def has_add_permission(self, request):
        return False

admin.site.register(Imovel,ImovelAdmin)