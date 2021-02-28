import os
import sys
import time
import random
import adb
import findimg
import check
import click



adb.connect_adb()
while True:
    time.sleep(0.7)
    t = check.fight()  # 检查当前页面状态
    time.sleep(1)
    click.on_fight(t)  # 根据状态执行命令
