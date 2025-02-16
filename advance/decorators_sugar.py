def pretty_sumab(func):
    def wrapper(a,b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a,b)
    return wrapper


@pretty_sumab
def sumab(a,b):
    summed = a + b


sumab(23, 1)

if __name__ == "__main__":
    sumab(23, 1)


