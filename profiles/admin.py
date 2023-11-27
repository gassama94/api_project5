from django.contrib import admin
from .models import Profile, Project, Task

# Register your models here.
admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_at', 'updated_at', 'name')
    search_fields = ('name', 'owner__username')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'owner__username')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'project', 'completed', 'created_at', 'updated_at')
    search_fields = ('text', 'project__title')

