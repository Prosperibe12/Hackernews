from django.urls import path 
from . import views
from rest_framework.urlpatterns import format_suffix_patterns 

urlpatterns = [
    path('story/', views.getStories, name='stories'),
    path('job/', views.getJobStories, name='jobs'),
    path('asks/', views.getAskStories, name='asks'),
    path('story/<str:id>/', views.singleStory, name='single-story'),
    path('job-details/<str:id>/', views.singleJobStory, name='job-details'),
    path('ask-details/<str:id>/', views.singleAskStory, name='ask-details'),
    path('addstory/', views.addStory, name='addstory'),
    path('addjob/', views.addJob, name='addjob'),
    path('addask/', views.addAskStories, name='addask'),
    path('updatestory/<str:id>/', views.updateStory, name='updatestory'),
    path('updatejob/<str:id>/', views.updateJob, name='updatejob'),
    path('updateask/<str:id>/', views.updateAskStory, name='updateask'),
    path('deletestory/<str:id>/', views.deleteStory, name='deletestory'),
    path('deletejob/<str:id>/', views.deleteJobStory, name='deletejob'),
    path('deleteask/<str:id>/', views.deleteAskStory, name='deleteask')
]
urlpatterns = format_suffix_patterns(urlpatterns)