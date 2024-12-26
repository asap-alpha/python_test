import random


# def sum(x,y):
#     return float(x) + float(y)
#
# print(f"sum: {sum(2,9)}")
#
# dictionary = {
#     "name": "Asap",
#     "age":20,
#     "summary": random.choices(["developer", "designer", "engineer", "tester"], k=1)[0]
# }
# #iterate over and display the various key => value
#
# def dictionary_key_value(dic):
#     for key, value in dic.items():
#         print(f"{key} => {value}")
#
# dictionary_key_value(dictionary)

def replace_last_name(last_nam):
    full_name = "Asap Dasty"
    split_full_name = full_name.split(" ")
    print(f"full name: {split_full_name}")
    split_full_name[-1] = last_nam

    current_name = " ".join(split_full_name)
    print(f"updated name: {current_name}")
    return current_name


print(f"split full name {replace_last_name("Mustapha")}")
