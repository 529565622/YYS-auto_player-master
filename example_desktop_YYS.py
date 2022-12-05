import time, os
import auto_player as player


def auto_play_yuhun(rounds=999):
    count = 0
    while count < rounds:
        ar1 = ['acks', 'aczd', 'actg', 'tg']
        re = player.find_touch_any(ar1, True, True, 3)
        if re == 'actg':
            count + 1


if __name__ == '__main__':
    auto_play_yuhun()
