from django.contrib import admin
from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'designation', 'created_at')
    list_display_links = ('id', 'first_name')
    search_fields = ('id', 'first_name','Last_name','designation')
    
admin.site.register(Team, TeamAdmin)