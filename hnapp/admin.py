from django.contrib import admin
from .models import Stories, JobStories, AskStories

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'by',
        'decendants',
        'storyid',
        'score',
        'storytime',
        'title',
        'type',
        'url',
        'source'
    )
    
class AskStoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'by',
        'decendants',
        'askId',
        'kids',
        'score',
        'text',
        'time',
        'title',
        'type',
        'source'
    )
    
class JobStoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'by',
        'jobIds',
        'score',
        'time',
        'title',
        'type',
        'url',
        'source'
    )

admin.site.register(Stories, StoryAdmin)
admin.site.register(JobStories, JobStoryAdmin)
admin.site.register(AskStories, AskStoryAdmin)
