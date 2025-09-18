# AS 2nd boolean notes :D
# bool() gives boolean value of specified object

import time
import datetime as DT

current_time = time.time()

readable = time.ctime(current_time)

print(f"Current time in seconds since Jan 1st 1970: {current_time}")
print(f"Current time: {readable}")

now = DT.datetime.now()

print(f"{now}")