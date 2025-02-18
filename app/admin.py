from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from app.models import Department, Employee


admin.site.register(Department, MPTTModelAdmin)
admin.site.register(Employee)
