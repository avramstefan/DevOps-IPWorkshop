import time
import os

SLEEP_TIME = 5

def main():
    print("This is the first text. You have to wait " + str(SLEEP_TIME) + " seconds")

    time.sleep(SLEEP_TIME)

    print("This is the second text. Exiting now...")

    os._exit(-1)


if __name__ == "__main__":
    main()
