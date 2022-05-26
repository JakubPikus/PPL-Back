from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from faceitUpdater import faceitApi



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(faceitApi.update_match, 'interval', minutes=1)
    scheduler.start()