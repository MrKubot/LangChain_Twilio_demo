from django.contrib import admin
from .models import SMSLog

# Register your models here.

@admin.register(SMSLog)
class SMSLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'status', 'created_at')
    list_filter = ('status', 'employee__role')
    search_fields = ('employee__first_name', 'employee__last_name')
    readonly_fields = ('created_at',)