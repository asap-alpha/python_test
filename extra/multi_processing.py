import multiprocessing as mp
import time


def random_million(numbers):
    for number in numbers:
        print(number)

if __name__ == "__main__":
    print("we're waiting")
    t = mp.Process(target= random_million, args = (range(1000),))
    t.start()
    time.sleep(2)
    print("we're here!")
    print(len(t.__annotations__))
    t.join()
