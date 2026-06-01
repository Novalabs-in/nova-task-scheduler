from apscheduler.schedulers.background import BackgroundScheduler
import time

def periodic_cleanup_task():
    print("Running scheduled repository database cleanup...")

scheduler = BackgroundScheduler()
scheduler.add_job(periodic_cleanup_task, 'interval', minutes=10)

if __name__ == "__main__":
    scheduler.start()
    print("Scheduler started. Periodic cleanups active.")
