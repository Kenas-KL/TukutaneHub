from django.contrib import admin

from .models import SectionActivity, Enterprise, Service, Request


# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_enterprise', 'email', 'phone')

class SectionActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Request, RequestAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SectionActivity, SectionActivityAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)

