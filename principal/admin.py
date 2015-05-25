from django.contrib import admin
from models import *
class UsuarioAdminView(admin.ModelAdmin):
    fieldsets = (
        ('Usuario', {
            'fields': ('first_name','last_name', 'username', 'email' ,'password','birth',)
        }),
    )
    list_display = ['__unicode__','first_name','email','date_joined']

class PhoneAdminView(admin.ModelAdmin):
    fieldsets = (('Telefonos',{'fields':('name','image','caracteristics_that_own','price_that_has','visitas','puntuaction_that_has')}),)
    list_display = ['__unicode__','visitas','tiempo_registro']

class caracteristicAdminView(admin.ModelAdmin):
    list_display = ['__unicode__','type','information']
# Register your models here.
admin.site.register(punctuacion)
admin.site.register(client,UsuarioAdminView)
admin.site.register(caracteristic,caracteristicAdminView)
admin.site.register(price)
admin.site.register(phone,PhoneAdminView)