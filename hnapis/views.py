from rest_framework.decorators import api_view 
from .serializers import StorySerializer, JobStorySerializer, AskStorySerializer
from rest_framework.response import Response 
from rest_framework import status 
from hnapp.models import Stories, AskStories, JobStories


"""
All API GET ENDPOINT
"""
# list all stories
@api_view(['GET'])
def getStories(request, format=None):
    
    # fetch all story
    stories = Stories.objects.all()
    # serialize story
    storyserialize = StorySerializer(stories, many=True)
    return Response(storyserialize.data)

# list all jobs
@api_view(['GET'])
def getJobStories(request, format=None):
    
    # fetch all jobs from database
    job = JobStories.objects.all()
    # serialize jobs object
    jobserialize = StorySerializer(job, many=True)
    return Response(jobserialize.data)

# list all jobs
@api_view(['GET'])
def getAskStories(request, format=None):
    
    # fetch all askstories from database
    ask = AskStories.objects.all()
    # serialize askstory object
    askserialize = AskStorySerializer(ask, many=True)
    return Response(askserialize.data)

"""
All API GET BY FILTER ID
"""
# filter story id
@api_view(['GET'])
def singleStory(request, id):
    
    try:
        singlestory = Stories.objects.get_single_story(id=id)
    except Stories.DoesNotExist:
        return Response(status=404)
    
    singlestoryserialize = StorySerializer(singlestory)
    return Response(singlestoryserialize.data)

# filter job by id
@api_view(['GET'])
def singleJobStory(request, id):
    
    try:
        singlejobstory = JobStories.objects.get_single_job(id=id)
    except JobStories.DoesNotExist:
        return Response(status=404)
    
    singlejobserialize = JobStorySerializer(singlejobstory)
    return Response(singlejobserialize.data)

# filter askstory by id
@api_view(['GET'])
def singleAskStory(request, id):
    
    try:
        singleaskstory = AskStories.objects.get_single_ask(id=id)
    except AskStories.DoesNotExist:
        return Response(status=404)
    
    singleaskserialize = AskStorySerializer(singleaskstory)
    return Response(singleaskserialize.data)

"""
All POST METHOD FOR TOPSTORIES, JOBS, ASKSTORIES 
"""
# add stories
@api_view(['POST'])
def addStory(request, format=None):

    # get data from request data
    storyserializer = StorySerializer(data=request.data)
    # call the valid method to valid posted data
    if storyserializer.is_valid():
        storyserializer.save()
        return Response(storyserializer.data, status=status.HTTP_201_CREATED)
    
    return Response(storyserializer.errors, status=status.HTTP_400_BAD_REQUEST)

# add job
@api_view(['POST'])
def addJob(request, format=None):

    # get data from request data
    jobserializer = JobStorySerializer(data=request.data)
    # call the valid method to valid posted data
    if jobserializer.is_valid():
        jobserializer.save()
        return Response(jobserializer.data, status=status.HTTP_201_CREATED)
    
    return Response(jobserializer.errors, status=status.HTTP_400_BAD_REQUEST)

# add ask stories
@api_view(['POST'])
def addAskStories(request, format=None):

    # get data from request data
    askserializer = AskStorySerializer(data=request.data)
    # call the valid method to valid posted data
    if askserializer.is_valid():
        askserializer.save()
        return Response(askserializer.data, status=status.HTTP_201_CREATED)
    
    return Response(askserializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
All UPDATE METHOD FOR TOPSTORIES, JOBS, ASKSTORIES
Prevent hackernews data from been updated
"""
# update method for stories
@api_view(['PUT'])
def updateStory(request, id):
    
    try:
        story = Stories.objects.get(id=id) 
    except Stories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    storyserialize = StorySerializer(instance=story, data=request.data)
    if storyserialize.is_valid():
        # prevent update if source is Hackernews
        newsource = storyserialize.validated_data.get('source')
        if newsource == "Hackernews":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            storyserialize.save()
        return Response(storyserialize.data, status=status.HTTP_201_CREATED)
    
    return Response(storyserialize.errors, status=status.HTTP_400_BAD_REQUEST)

# update method for stories
@api_view(['PUT'])
def updateJob(request, id):
    
    try:
        jobstory = JobStories.objects.get(id=id) 
    except JobStories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    jobserialize = JobStorySerializer(instance=jobstory, data=request.data)
    if jobserialize.is_valid():
        # prevent update if source is Hackernews
        newsource = jobserialize.validated_data.get('source')
        if newsource == "Hackernews":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            jobserialize.save()
        return Response(jobserialize.data, status=status.HTTP_201_CREATED)
    
    return Response(jobserialize.errors, status=status.HTTP_400_BAD_REQUEST)

# update method for stories
@api_view(['PUT'])
def updateAskStory(request, id):
    
    try:
        askstory = AskStories.objects.get(id=id) 
    except AskStories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    askserialize = AskStorySerializer(instance=askstory, data=request.data)
    if askserialize.is_valid():
        # prevent update if source is Hackernews
        newsource = askserialize.validated_data.get('source')
        if newsource == "Hackernews":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            askserialize.save()
        return Response(askserialize.data, status=status.HTTP_201_CREATED)
    
    return Response(askserialize.errors, status=status.HTTP_400_BAD_REQUEST)

"""
All DELETE METHOD FOR TOPSTORIES, JOBS, ASKSTORIES
Prevent hackernews data from been deleted
"""
# delete method for stories
@api_view(['DELETE'])
def deleteStory(request, id):
    
    try:
        askstory = Stories.objects.get(id=id) 
    except Stories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if askstory.source == "Hackernews":
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        askstory.delete()
    
    return Response("Item Deleted Successfully")

# delete method for jobs
@api_view(['DELETE'])
def deleteJobStory(request, id):
    
    try:
        jobstory = JobStories.objects.get(id=id) 
    except JobStories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if jobstory.source == "Hackernews":
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        jobstory.delete()
    
    return Response("Item Deleted Successfully")

# delete method for askstory
@api_view(['DELETE'])
def deleteAskStory(request, id):
    
    try:
        askstory = AskStories.objects.get(id=id) 
    except AskStories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if askstory.source == "Hackernews":
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        askstory.delete()
    
    return Response("Item Deleted Successfully")