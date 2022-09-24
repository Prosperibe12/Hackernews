from django.db import models
from .managers import *
# Create your models here.
class Stories(models.Model):
    STORY_SOURCE = (
        ('Hackernews', 'Hackernews'),
        ('User', 'User')
    )
    by = models.CharField(max_length=200, null=True, blank=True)
    decendants = models.CharField(max_length=200, null=True, blank=True)
    storyid = models.CharField(max_length=150, null=True, blank=True)
    score = models.CharField(max_length=200, null=True, blank=True)
    storytime = models.CharField(max_length=200, null=True, blank=True)
    title = models.TextField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    source = models.CharField(max_length=100, choices=STORY_SOURCE, default='Hackernews', null= False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = StoryManager()
    
    def __str__(self):
        return self.by 
    
# model for job stories
class JobStories(models.Model):
    
    JOB_SOURCE = (
        ('Hackernews', 'Hackernews'),
        ('User', 'User')
    )
    by = models.CharField(max_length=150, blank=True, null=True)
    jobIds = models.CharField(max_length=150, blank=True, null=True)
    score = models.CharField(max_length=150, blank=True, null=True)
    time = models.CharField(max_length=150, blank=True, null=True)
    title = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=150, blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    source = models.CharField(max_length=100, choices=JOB_SOURCE, default='Hackernews', null= True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = JobsManager()
    
    def __str__(self):
        return self.by 
    
# model for ask stories
class AskStories(models.Model):
    
    ASK_SOURCE = (
        ('Hackernews', 'Hackernews'),
        ('User', 'User')
    )
    by = models.CharField(max_length=150, blank=True, null=True)
    decendants = models.CharField(max_length=150, blank=True, null=True)
    askId = models.CharField(max_length=150, blank=True, null=True)
    kids = models.JSONField(null=True, blank=True)
    score = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    type = models.CharField(max_length=150, blank=True, null=True)
    source = models.CharField(max_length=100, choices=ASK_SOURCE, default='Hackernews', null= True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = AskStoryManager()
    
    def __str__(self):
        return self.by 
    
