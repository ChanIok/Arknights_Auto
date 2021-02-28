import random
import time
import sys
import os
import adb


def sleep_randtime(a, b):
    """产生a,b间的随机时间延迟"""
    time.sleep(random.uniform(a, b))


def click(x, y):
    """输入两个二维列表，表示要点击的位置的x坐标，y坐标"""
    cmd_click = 'adb shell input tap {} {}'.format(x, y)
    os.system(cmd_click)
    sleep_randtime(1.2, 2.3)  # 随机延迟


def init_xy():
    xr = 0
    yr = 0


def on_fight(t):
    if t == 1:
        xr = random.randint(1200, 1400)
        yr = random.randint(630, 680)
        print('---进入编队---')
        click(xr, yr)
    if t == 2:
        xr = random.randint(1120, 1245)
        yr = random.randint(365, 640)
        print('---开始行动---')
        click(xr, yr)
    if t == 3:
        xr = random.randint(20, 1400)
        yr = random.randint(30, 430)
        print('---结束行动---')
        click(xr, yr)
    if t == 4:
        adb.kill()
        print('---缺少理智，退出程序---')
        sys.exit()


def on_visit(t):
    if t == 101:
        xr = random.randint(300, 435)
        yr = random.randint(560, 595)
        print('---打开个人名片---')
        click(xr, yr)
    if t == 102:
        xr = random.randint(25, 205)
        yr = random.randint(190, 255)
        print('---打开好友列表---')
        click(xr, yr)
    if t == 103:
        xr = random.randint(945, 1050)
        yr = random.randint(120, 205)
        print('---访问好友基建---')
        click(xr, yr)
    if t == 109:
        xr = random.randint(1255, 1435)
        yr = random.randint(580, 675)
        print('---访问下位好友---')
        click(xr, yr)
    if t == 105:
        xr = random.randint(170, 365)
        yr = random.randint(15, 55)
        print('---访问已达上限，准备返回主页---')
        click(xr, yr)
    if t == 106:
        xr = random.randint(155, 195)
        yr = random.randint(150, 320)
        print('---返回主页---')
        click(xr, yr)
        sys.exit()