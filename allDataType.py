data = {
    "name": "Asap dasty", #string
    "age": 30,  # int
    "is_active": True,  # bool
    "grades": [85, 90, 88],  # list
    "address": ("Street", 123),  # tuple
    "height": 5.5,  # float
    "siblings": {"Bob", "Charlie"},  # set
    "profile_picture": None  # None
}

for value in data.values():
    print(f"{value}")
    if isinstance(value, set):
        print("value is set")
        for num in value:
            print(f"num:{num}")
