def person(func):
    print(f"func received {func}")
    def name(*args):
        print("The current user is : ", end="")
        func(*args)
    return name


def user_name(name):
    print(f"my name is {name}")

if __name__ == "__main__":
    myObj = person(user_name)
    myObj("Abdallah")

