#!/usr/bin/python3
def main_f(*argv):
    if len(argv) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv)))
        for i,v in enumerate(argv):
            print("{}: {}".format(i,v))
    # 1: Hello
    # print(len(arg))
if __name__ == "__main__":
    import sys
    main_f(sys.argv[1])