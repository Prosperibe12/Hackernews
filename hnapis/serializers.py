from rest_framework import serializers
from hnapp.models import Stories, AskStories, JobStories

class StorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stories 
        fields = ['id','by', 'storyid', 'score', 'title', 'type', 'url','source']
        
class AskStorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AskStories 
        fields = ['id','by','askId', 'score', 'text', 'title', 'type','source']
        
class JobStorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobStories 
        fields = ['id','by', 'jobIds', 'score', 'title', 'type', 'url','source']
        
