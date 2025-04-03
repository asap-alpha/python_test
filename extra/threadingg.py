import threading as thread
import time


def random_numbers(numbers):
    for number in numbers:
        print(number)


if __name__ == "__main__":
    print("we're starting")
    t = thread.Thread(target= random_numbers, args = (range(1000),))
    t.start()
    time.sleep(2)
    t.join()
    print("we're ending here!")
    print(t.name)

