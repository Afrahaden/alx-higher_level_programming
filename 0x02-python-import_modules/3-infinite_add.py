#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = sys.argv
    result = 0
    for arg in range(len(arguments)):
        if arg > 0:
            result += int(arguments[arg])
    print("{}".format(result))
