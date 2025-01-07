#default value

def default_function(name, age = 24):
    print("name: {}".format(name))
    print("age: {}".format(age))


# default_function("Asap")
# default_function(name="Asap",age=30)

def append_to_List(nums, numericlist = []):
    numericlist.append(nums + 1)
    return numericlist


# newValue = append_to_List(20)
# print("newValue {}".format(newValue))

#keyword parameters
'keyword parameter as function is not much different from default function but arguments preside with placeholder.'

def division(num, denum):
    try:
        result = num / denum
        print("num: {} denum: {} => result: {} ".format(num, denum, result))
    except ZeroDivisionError as e:
        print("{}".format(e))
    except ValueError as e:
        print("{}".format(e))
    except Exception as e:
        print("{}".format(e))

# division(num= 10, denum= 2)

#keyword-only function preside with asterisk
def interest(amount,*,rate, point):
    result =amount*(1 / rate)
    print("amount: {} rate: {} result: {} point: {}".format(amount, rate, result, point))


interest(100,rate=30, point= 10)




