strings = ["Testing", "Testing the test"]

for string in strings:
    if(string.endswith("test")):
        print("found test")
    else:
        print("not found")