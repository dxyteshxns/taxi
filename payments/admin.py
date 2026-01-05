from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('trip','amount','method','status','created_at')
    list_filter = ('status','method')
    search_fields = ('trip__id','transaction_id')
