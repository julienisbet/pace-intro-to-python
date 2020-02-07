SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE*60
SECONDS_IN_DAY = SECONDS_IN_HOUR*24
SECONDS_IN_WEEK = SECONDS_IN_DAY*7
def format_seconds(seconds):
  weeks = seconds // SECONDS_IN_WEEK
  seconds -= weeks * SECONDS_IN_WEEK

  days = seconds // SECONDS_IN_DAY
  seconds -= days * SECONDS_IN_DAY

  hours = seconds // SECONDS_IN_HOUR
  seconds -= hours * SECONDS_IN_HOUR

  minutes = seconds // 60
  seconds -= minutes * 60

  return(f"{weeks}w {days}d {hours}h {minutes}m {seconds}s")


print(format_seconds(45))      #'45s'
print(format_seconds(175))     #'2m 55s'
print(format_seconds(1234))    #'20m 34s'
print(format_seconds(10815))   #'3h 0m 15s';
print(format_seconds(12345))   #'3h 25m 45s'
print(format_seconds(1210459)) #'2w 0h 14m 19s'



