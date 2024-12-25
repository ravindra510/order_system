from celery import shared_task
from datetime import datetime

@shared_task
def daily_task():
    print("Daily task running at", datetime.now())










# from celery import shared_task
# import datetime
# from django.utils.timezone import localtime

# @shared_task
# def run_daily_task():
#     current_time = localtime(datetime.datetime.now())
#     if current_time.hour == 14 and current_time.minute == 30:
#         print("Daily Task is running at 2:30 PM")
#         # Add your logic here to handle the background task
#     return "Task Completed"
