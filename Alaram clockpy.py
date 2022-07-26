# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 16:03:12 2021

@author: Gaurav Dua
"""

import os
import datetime
import time
n=1
c,b,a=input("Enter the Date = ").split("/")
hr, minn , sec =input("Enter the Time =").split( ":" )
shedule_date =datetime.date(int(a),int(b),int(c))
while n>0:
    if time.localtime().tm_hour==int(hr) and time.localtime().tm_min==int(minn) and time.localtime().tm_sec==int(sec) and datetime.date.today()==shedule_date:
        os.startfile("D:\\Movie\\m.mkv") # enter the path 
        print("Alarm Ringing......")
        break
else:
    n+=1