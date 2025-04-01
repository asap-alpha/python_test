data = []
# for i in data[:]:
#     if i % 2:
#         data.append(i)
#
#     print(data)

data.append([i for i in range(10) if i % 2 == 0])
print(data)
