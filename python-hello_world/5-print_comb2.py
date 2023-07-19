for i in range(100):
    print("{:02d}".format(i), end=', ' if i < 99 else '\n')
# :2d means make their len 2 digits 0->00 11 ->11