from django.contrib import admin
from .models import AuditReport

class AuditReportAdmin(admin.ModelAdmin):
    list_display = ('factory_name', 'audit_date', 'defect_count')
    search_fields = ('factory_name',)
    list_filter = ('audit_date',)

admin.site.register(AuditReport, AuditReportAdmin)