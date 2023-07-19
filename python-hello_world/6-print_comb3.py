for i in range(90):
    if i%10 ==0:
        continue
    print("{:02d}".format(i), end=', ' if i < 89 else '\n')
# :2d means make their len 2 digits 0->00 11 ->11