squares = ((value, value*2) for value in range(10) if value % 2 == 0)
for val, multi in squares:
    print(f"value: { val} multi: {multi}")

print(f"##########################################################")
list_squares = [(value, value*2) for value in range(10) if value % 2 != 0]

for key, value in list_squares:
    print(f"value: {key} multiply: {value}")

print("$$$$$$$$$$$$$$")

print(type({'key':'data'}))