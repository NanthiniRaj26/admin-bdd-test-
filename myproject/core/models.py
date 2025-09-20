from django.db import models

class AuditReport(models.Model):
    factory_name = models.CharField(max_length=100)
    audit_date = models.DateField()
    defect_count = models.IntegerField()
