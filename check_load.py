#!/usr/bin/python3.8
# Python program to explain os.getloadavg() method  
  
# importing os module 
import os
from conf import *
# Get the load average over
# the last 1, 5, and 15 minutes 
# using os.getloadavg() method
load1, load5, load15 = os.getloadavg()
total_cpu=os.cpu_count()
tereshold = 1.5*tereshold_cpu

# Print the load average over
# the last 1, 5, and 15 minutes 
print("Load average over the last 1 minute:", load1)
print("Load average over the last 5 minute:", load5)
print("Load average over the last 15 minute:", load15)

# print(tereshold)
if load5 >= tereshold :
    print("load is high" , load5)
else :
    print("load is:", load5)