#!/usr/bin/python3.8
import subprocess
import info
import sms
from conf import *
ip=info.get_ip()
df = subprocess.Popen(['df','-h'],stdout=subprocess.PIPE)

def disk_checker():

    for line in df.stdout:
        
        mount_point = line.decode().split()

        directory = mount_point[5]
        size_use = mount_point[4][:-1]


        list_dir = {"/":threshold_slash , "/var":threshold_var, "/tmp":threshold_tmp , "/home" :threshold_home, "/home/services":threshold_home_services , "/backup":threshold_backup , "/home/data":threshold_home_data , "/home/devops/archive":threshold_devops_archive }

        if size_use != "Use" and directory  in list_dir :

            size = int(size_use)
            if size >= list_dir[directory]:
                print("Disk Free Size above",list_dir[directory],directory,mount_point[4])
                for iter in team:
                    sms.send_sms(nums=team[iter],name=iter,server=ip,dir=directory+" is: "+size_use)
            else:
                print("Disk Free Normal Size",directory,mount_point[4])


disk_checker()