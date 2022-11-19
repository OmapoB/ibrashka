def _1_5_3():
    print(11111*1111111)
def _1_5_5():
    print(42/(4+2*(-2)))
def _1_5_7():
    print(2014**14)
def _1_6_5():
    print(2014.0 **14)
def _1_6_6():
    print(7/3)
def _1_8_6():
    x = int(input())
    y = int(input())
    all_sleep = x * 60 + y
    print(all_sleep)
def _1_8_7():
    x = int(input())
    hours = x // 60
    minutes = x - hours * 60
    print(hours)
    print(minutes)
def _1_8_8():
    x = int(input())
    H = int(input())
    M = int(input())
    slept_time = H * 60 + M
    stand_time = slept_time + x
    hours = stand_time // 60
    minutes = stand_time - hours * 60
    print(hours)
    print(minutes)
if __name__ == '__main__':
    _1_8_8()
