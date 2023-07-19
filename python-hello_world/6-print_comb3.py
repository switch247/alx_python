for i in range(90):
    if i > int(str(i)[::-1]):
        continue
    print("{:02d}".format(i), end=', ' if i < 89 else '\n')
# :2d means make their len 2 digits 0->00 11 ->11

# you cant have 23 and 32 together