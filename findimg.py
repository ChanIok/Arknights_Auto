import os
import cv2
import time


def get_screen():
    cmd_get = 'adb shell screencap -p /sdcard/screen_img.png>nul 2>nul'  # 截屏口令
    cmd_send = 'adb pull sdcard/screen_img.png ./images>nul 2>nul'  # 发送图片口令
    os.system(cmd_get)  # 截屏和发送操作
    os.system(cmd_send)
    


def match_img(template):
    img = cv2.imread('./images/screen_img.png', 0)
    template = cv2.imread('./images/{}'.format(template), 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)  # 图像模板匹配函数
    maxres = res.max()  # maxres大于0.9即可认为模板在匹配图像中出现
    if maxres >= 0.9:
        return 1
    else:
        return 0
