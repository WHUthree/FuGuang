from apscheduler.schedulers.background import BackgroundScheduler

#判定招募信息是否过期
overdue_scheduler = BackgroundScheduler()
overdue_scheduler.start()