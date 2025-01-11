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


# interest(100,rate=30, point= 10)

def addition(x: int, y: str):
    result = x + int(y)
    print("x -> {} y -> {} result -> {}".format(x,y,result))

# addition(2, "1")

# keyword-only and some positional-only arguments
def check_result(x,/,y,*,constant):
    result =y - x + constant
    print("x -> {} y -> {} result -> {}".format(x,y,result))


# check_result(20, y =20, constant =1)


#arbitrary functions *args(positional arguments)
def random_arg(*rand):
    result = 0
    for v in rand:
        result = v + result
    return result


result = random_arg(10,23,11,45,20)
# print("{}".format(result))


# **kwargs(keyword arguments)
def random_kwargs(**kwargs):
    #details = {}
    details = []
    for k,v in kwargs.items():
        details.append((k,v))
    return details

kwargs_result = random_kwargs(name = "Asap", age = 12, homeTown = "Ksi", country = "Ghana")
print("{}".format(kwargs_result))