import os
import sys


def connect():
    r = os.system('adb connect 127.0.0.1:7555')


def connect_check():
    r = os.popen('adb devices')
    info = r.readlines()
    if info[1]=='\n':
        return 0
    else:
        return 1


def kill():
    r = os.system('adb kill-server')

def connect_adb():
    c = connect_check()
    if c == 0:
        print('尝试连接模拟器')
        connect()
        c = connect_check()
        if c == 0:
            print('连接模拟器失败，请检查错误')
            sys.exit()
        else:
            print('连接模拟器成功')
    else:
        print('模拟器已连接')