squares = ((value, value*2) for value in range(10) if value % 2 == 0)
for val, multi in squares:
    print(f"value: { val} multi: {multi}")