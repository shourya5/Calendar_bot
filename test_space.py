import datetime
today = datetime.datetime.utcnow()
print(today)
yesterday = datetime.datetime.combine(today, datetime.time())
x =  today.replace(hour=23, minute=59, second=59,microsecond=0) 
print(type(x))
end = x + datetime.timedelta(1)
print(end.isoformat())

