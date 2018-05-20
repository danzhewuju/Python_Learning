#!/usr/bin/python3
import time
tt = 1510850662716
tt //= 1000
t = int(time.time())
time_local=time.localtime(tt)
dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
print(dt)
t = int(time.time())
# print(t)