import sys
from time import sleep

if __name__ == "__main__":
    num = sys.argv[1]
    for i in range(num):
        print(str(i) + " " + str(i+1))
        sleep(1)


