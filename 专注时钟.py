import time
import os

#提示用户输入要专注的时间（单位为分钟）
focus_time = int(input("请输入要专注的时间（单位为分钟）："))

#将时间转换为秒
focus_time = focus_time * 60

#倒计时
while focus_time:
    #将秒数转换为分钟和秒数
    mins, secs = divmod(focus_time, 60)
    #格式化倒计时字符串
    timer = '{:02d}:{:02d}'.format(mins, secs)
    #打印倒计时字符串
    print(timer, end="\r")
    #暂停一秒
    time.sleep(1)
    #减少剩余时间
    focus_time -= 1

#倒计时结束时播放一段音乐提醒用户
os.system("afplay /System/Library/Sounds/Ping.aiff")
