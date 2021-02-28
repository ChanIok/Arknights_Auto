import findimg


def star_action():
    """检查是否开始行动界面"""
    if findimg.match_img('star_action.bmp') == 1:
        return 1
    else:
        return 0


def formation():
    """检查是否编队界面"""
    if findimg.match_img('formation.bmp') == 1:
        return 2
    else:
        return 0


def end_action():
    """检查是否结束界面"""
    if findimg.match_img('end_action.bmp') == 1:
        return 3
    else:
        return 0


def use_up():
    """检查是否用完理智"""
    if findimg.match_img('use_up.bmp') == 1:
        return 4
    else:
        return 0


def friends():
    """检查是否主页"""
    if findimg.match_img('my_friends.bmp') == 1:
        return 101
    else:
        return 0


def my_card():
    """检查是否个人名片"""
    if findimg.match_img('my_card.bmp') == 1:
        return 102
    else:
        return 0


def friends_list():
    """检查是否好友列表"""
    if findimg.match_img('friends_list.bmp') == 1:
        return 103
    else:
        return 0
def friends_home():
    """检查是否好友基建"""
    if findimg.match_img('friends_home.bmp') == 1:
        return 104
    else:
        return 0

def visit_limit():
    """检查是否访问上限"""
    if findimg.match_img('visit_limit.bmp') == 1:
        return 105
    else:
        return 0

def menu():
    """检查是否打开菜单"""
    if findimg.match_img('menu.bmp') == 1:
        return 106
    else:
        return 0

def fight():
    t = 0
    findimg.get_screen()
    t += star_action()
    t += formation()
    t += end_action()
    t += use_up()
    return t
