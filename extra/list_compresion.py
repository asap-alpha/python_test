from funcs.function_more import append_to_List

fresh_Fruit = ['banana', 'loganberry ', 'passion fruit']

[print(fruit.capitalize()) for fruit in fresh_Fruit]

# squares = []
# for x in range(10):
#     squares.append(x**2)
#
# squares

square = []
[square.append(x*2) for x in range(10) ]

result = list(map(lambda x: x**2, range(10)))
# print(f"result:=> {result}")

res = [x+2 for x in range(10)]
print(f"res:=> {res}")

compose = []
output = [ compose.append((x, y)) for x in [1,2,3] for y in [3,1,4] if x == y]

# print(f"output {len(output)} => {compose}")

combine = []
for x in [1,2,3]:
    for y in [3,1,4]:

        if x != y:
            combine.append((x,y))
            break
        else:
            combine.append((x,y))


print(f"combine {combine}")