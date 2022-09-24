from django.db import models 

class HNNewsQuerySet(models.QuerySet):
    
    def get_single_story(self,id):
        return self.get(id=id)
    
    def get_single_job(self,id):
        return self.get(id=id)
    
    def get_single_ask(self,id):
        return self.get(id=id)


class StoryManager(models.Manager):
    
    def get_queryset(self) :
        return HNNewsQuerySet(self.model, using=self._db)

    def get_single_story(self,id):
        return self.get_queryset().get_single_story(id=id)

class JobsManager(models.Manager):
    
    def get_queryset(self):
        return HNNewsQuerySet(self.model, using=self._db)
    
    def get_single_job(self,id):
        return self.get_queryset().get_single_job(id=id)
    
class AskStoryManager(models.Manager):
    
    def get_queryset(self):
        return HNNewsQuerySet(self.model, using=self._db)
    
    def get_single_ask(self,id):
        return self.get_queryset().get_single_ask(id=id)
    
    