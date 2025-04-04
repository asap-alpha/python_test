import threading as thread
import time


def random_numbers(numbers):
    for number in numbers:
        print("we're starting")
        time.sleep(2)
        print("we're ending here!")



t = thread.Thread(target=random_numbers, args=(range(10),))

t.start()

# t.join()

print(f"total thread {thread.active_count()}")

