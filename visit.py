import findimg
import click
import check
import time
import adb


def friends():
    """访问好友基建"""
    c = 0
    while True:
        t = 0
        time.sleep(0.6)
        findimg.get_screen()
        t += check.friends()
        t += check.my_card()
        t += check.friends_list()
        t += check.friends_home()
        click.on_visit(t)
        if t == 104:#已访问第一位好友
            break
    while True:  # 循环访问下一位，直到访问达到上限或者计数返回
        t = 0
        time.sleep(0.8)
        findimg.get_screen()
        t = check.visit_limit()
        click.on_visit(109)
        c += 1
        if t == 105 or c >= 15:
            break  # 退出访问循环
    while True:  # 返回主页
        click.on_visit(t)
        time.sleep(0.6)
        findimg.get_screen()
        tt = check.menu()
        if tt != 0:
            click.on_visit(tt)


adb.connect_adb()
friends()
