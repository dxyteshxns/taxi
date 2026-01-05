from django.contrib import admin
from .models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('id','rider','driver','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('rider__email','driver__user__email','origin','destination')
