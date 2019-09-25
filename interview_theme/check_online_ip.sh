#!/bin/bash
# 写一个脚本, 判断 192.168.1.0/24 网路里面, 当前在线 ip 有哪些


for ((I=1;I<=255;I++ ));do
    ping -c 2 -w 2 10.90.93.$I & >/dev/null
    if [ $? -eq 0 ];then
       echo -e "\033[32;40m10.90.93.$I is up.\033[0m"
    else
       echo -e "\033[31;40m10.90.93.$I is down.\033[0m"
    fi
done
