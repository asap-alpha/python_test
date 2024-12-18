# # int, float, double
# x = 1
# y = 20
# y = input("enter value to override <Y>")
#
# sum = x+ float(y)
# print(f"value {sum}")


# string
name = "Asap Dasty"
find = name.find("a")
other = name.split()
full_name = []
for split in other:
    full_name.append(split)
    if len(split) <= 2:
        print(f"split {split}")

print(f"full name {str(full_name)}")
print(other)
print(name)
