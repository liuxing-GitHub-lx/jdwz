import time
from datetime import datetime


print(time.asctime(time.localtime()))
print(time.ctime(time.time()))

print(datetime.now())
print(datetime.today())



a = "sninsdidf ngind:1/2"
idx = a.find('/')
print(a[idx+1:])