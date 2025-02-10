name = "asap dasty"
const = {"©", "¥", "é", "@", "→"}
print(ascii(const))

for i in range(5):
    if(i > 3):
        continue
    else:
        print(f"value is still less than {i}")


for i in range(5):
    if(i > 3):
        pass
    else:
        print(f"value is still less than {i}")


for i in range(5):
    if(i > 3):
        break
    else:
        print(f"value is still less than {i}")

