import time, os
import auto_player as player


def get_pictures():
    player.screen_shot()


def auto_play_yuhun(rounds=500):
    count = 0
    while count < rounds:
        ar1 = ['tz', 'hl', 'dm']
        re = player.find_touch_any(ar1)
        if re == 'tz':
            print('开始新一轮...')
            count += 1
            print(count)
            time.sleep(20)
            # re = player.find_touch_any(ar1, False)
            # if re == 'hl':
            #     time.sleep(13)
            # else:
            #     break
            ar2 = ['tg']
            i = 0
            while True:
                re1 = player.find_touch_any(ar2)
                # time.sleep(0.5)
                if re1 == 'tg':
                    i = i + 1
                if i == 2:
                    break
            i = 0
            ar3 = ['dm']
            while True:
                re3 = player.find_touch_any(ar3)
                # time.sleep(0.5)
                if re3 == 'dm':
                    i = i + 1
                if i == 2:
                    break


def function3():
    print('功能3未设置')


def menu(debug=False):
    menu_list = [
        [get_pictures, '获取当前屏幕截图'],
        [auto_play_yuhun, '自动刷图_御魂'],
        [function3, 'function3功能描述']
    ]

    start_time = time.time()
    print('程序启动，当前时间', time.ctime(), '\n')
    while True:
        i = 0
        for func, des in menu_list:
            msg = str(i) + ": " + des + '\n'
            print(msg)
            i += 1
        player.alarm(1)
        raw = input("选择功能模式：") if not debug else 1
        index = int(raw) if raw else 1
        func, des = menu_list[index]
        print('已选择功能： ' + des)
        func()


if __name__ == '__main__':
    auto_play_yuhun()
