# name = "Asap"
# age = input("Please enter you age! ")
# print(f"{name} welcome!, and Happy Birthday {age}")

x = input("enter value => ")
y = input("enter value => ")
total = float(x) + float(y)
print(f"total sum:: {total}")
while total > 20:
    if total >= 10:
        print("we have more than 10")
    else:
        print("we have less than 10")