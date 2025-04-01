def divide_num(numerator,denominator):
    divide = 0
    try:
        divide = float(numerator)/ int(denominator)

        divide = round(divide, 2)
        return divide
    except ZeroDivisionError:
        print("you can't divide by zero")

    finally:
        print(f"I'm staying here! {divide}")


#divide_num(2,2.2)

def round_num():
    try:
        value = float(input("enter a number >> "))
        value = round(value, 2)
        return value

    except ValueError as e:
        print(f"please enter a number: {e}")
        return None

    except Exception as e:
        print(f"any other exception happened::: {e}")
        return None


result = round_num()

if result is None:
    print("you didn't enter a number")
print(f"result is {result}")