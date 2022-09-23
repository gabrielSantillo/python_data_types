strings = ["Testing", "Testing the test"]

for string in strings:
    if (string.endswith("test")):
        print("found test")
    else:
        print("not found")

list_of_numbers = [15, 10, 5, 25, -10]

for number in list_of_numbers:
    if (number > 10):
        print("large:", number)
    else:
        print("not large:", number)

client = {
    "username": "Gabriel",
    "age": 26,
    "friends": ["Naty", "Chicago"]
}

print(client["username"], client["age"])

for friend in client["friends"]:
    print(friend)

list_of_clients = [
    {
        "username": "Gabriel",
        "age": 26,
        "friends": ["Naty", "Chicago"]
    },

    {
        "username": "Jose",
        "age": 56,
        "friends": ["Damaris", "Daniel"]
    },
]

for name in list_of_clients:
    print(name["username"], name["age"])
    for friend in name["friends"]:
        print(friend)

def number_function(one, two):
    return (one * two) / 2

result = number_function(10,10)
print(result)