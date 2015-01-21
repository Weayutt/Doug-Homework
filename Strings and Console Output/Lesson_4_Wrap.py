from datetime import datetime
now = datetime.now()

'%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
print '%s/%s/%s' % (now.month, now.day, now.year) + ' %s:%s:%s' % (now.hour, now.minute, now.second)

#This FANCY NEW AND IMPROVED program will make your lyfe 69X easier IT WILL (with no extra cost) TELL YOU THE TIME *clap* *clap*