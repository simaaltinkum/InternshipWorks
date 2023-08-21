from django.contrib import admin

from meseapp.models import WebSiteAyarlari, Items, Title, Email, Telephone, Services, Adresses

admin.site.register(WebSiteAyarlari)
admin.site.register(Items)
admin.site.register(Title)
admin.site.register(Email)
admin.site.register(Telephone)
admin.site.register(Services)
admin.site.register(Adresses)
# Register your models here.
