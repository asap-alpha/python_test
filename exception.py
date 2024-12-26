def divide_num(x,y):
    divide = 0
    try:
        divide = float(x)/ float(y)

        divide = round(divide, 4)
        return divide
    except ZeroDivisionError:
        print("you can't divide by zero")

    finally:
        print(f"I'm staying here! {divide}")


divide_num(2,1.1)
