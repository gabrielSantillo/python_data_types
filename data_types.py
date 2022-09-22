strings = ["Testing", "Testing the test"]

for string in strings:
    if(string.endswith("test")):
        print("found test")
    else:
        print("not found")

list_of_numbers = [15, 10, 5, 25, -10]

for number in list_of_numbers:
    if(number > 10):
        print("large:", number)
    else:
        print("not large:", number)