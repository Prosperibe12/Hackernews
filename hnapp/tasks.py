from __future__ import absolute_import, unicode_literals

from celery import shared_task
import requests 
import json 
from .models import Stories, AskStories, JobStories

"""
There different methods to achieve this task and also different points to consider based on API endpoints we make request to and also the performance of our application. I choose this method for simplicity.
Each Hackernews Endpoint returns a different object, most often the newstories and topstories end post will return items without the job or ask type. So i have decided to fetch from the endpoints separately since this application will host its on API.
"""
# function to fetch from hackernews api(topstories)
@shared_task
def get_story():
    baseUrl = 'https://hacker-news.firebaseio.com/v0'
    newStoriesUrl = f'{baseUrl}/newstories.json?print=pretty'
    itemUrl = f'{baseUrl}/item/'
    """
    make first request to the hackernews API(newstories endpoint)
    """
    response = requests.get(newStoriesUrl)
    if response.status_code == 200:
        storyIds = response.json()
        # making second request for each item returned
        count = 0
        for newStory in storyIds:
            count += 1
            if count == 8:
                break
            newUrl = itemUrl + str(newStory) + f'.json?print=pretty'
            newresponse = requests.get(newUrl)
            if newresponse.status_code == 200:
                item = newresponse.json()
                by = item['by']
                descendants = item['descendants']
                storyid = item['id']
                scores = item['score']
                time = item['time']
                titles = item['title']
                types = item['type']
                urls = item['url']
                Stories.objects.get_or_create(by=by, decendants=descendants, storyid=storyid, score=scores, storytime=time, title=titles, type=types, url=urls)
            
        return item 
    
# function for jobs api request
@shared_task(bind=True)
def get_jobs():
    
    baseUrl = 'https://hacker-news.firebaseio.com/v0'
    jobStoriesUrl = f'{baseUrl}/jobstories.json?print=pretty'
    itemUrl = f'{baseUrl}/item/'
    
    response = requests.get(jobStoriesUrl)
    if response.status_code == 200:
        jobids = response.json()
        # make second request
        counter = 0
        for ids in jobids:
            counter += 1
            if counter == 9:
                break
            newUrl = itemUrl + str(ids) + f'.json?print=pretty'
            newresponse = requests.get(newUrl)
            if newresponse.status_code == 200:
                jobs = newresponse.json()
                print("job::", jobs)
                job_by = jobs['by']
                print("by::", job_by)
                job_id = jobs['id']
                print("id::", job_id)
                job_score = jobs['score']
                print("job_score::", job_score)
                job_time = jobs['time']
                print("job_time::", job_time)
                job_title = jobs['title']
                print("job_title::", job_title)
                job_type = jobs['type']
                print("job_type::", job_type)
                job_url = jobs['url']
                print("job_url::", job_url)
                JobStories.objects.get_or_create(by=job_by, jobIds=job_id, score=job_score, time=job_time, title=job_title, type=job_type, url=job_url)
               
        return jobs
    
# function for jobs api request
@shared_task(bind=True)
def ask_stories():
    
    baseUrl = 'https://hacker-news.firebaseio.com/v0'
    askStoriesUrl = f'{baseUrl}/askstories.json?print=pretty'
    itemUrl = f'{baseUrl}/item/'

    response = requests.get(askStoriesUrl)
    if response.status_code == 200:
        askid = response.json()
                
        # make second request
        kounter = 0
        for ids in askid:
            kounter += 1
            if kounter == 5:
                break
            newUrl = itemUrl + str(ids) + f'.json?print=pretty'
            newresponse = requests.get(newUrl)
            if newresponse.status_code == 200:
                ask = newresponse.json()
                # print("ask::", ask)
                ask_by = ask['by']
                ask_desc = ask['descendants']
                ask_id = ask['id']
                ask_kid = ask['kids']
                ask_score = ask['score']
                ask_text = ask['text']
                ask_time = ask['time']
                ask_title = ask['title']
                ask_type = ask['type']
                AskStories.objects.get_or_create(by=ask_by, decendants=ask_desc, askId=ask_id, kids=ask_kid, score=ask_score, text=ask_text, time=ask_time, title=ask_title, type=ask_type)
                
        return ask
                
                
                
                
        
        
                
               
