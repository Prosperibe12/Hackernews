from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .apis import get_story, get_jobs, ask_stories

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(get_story, 'interval', seconds=18)
	scheduler.start()

def starts():
	scheduler = BackgroundScheduler()
	scheduler.add_job(ask_stories, 'interval', seconds=30)
	scheduler.start()
