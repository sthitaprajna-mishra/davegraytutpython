def hello_world():
    print("Hello World!")

hello_world()

def sum(num1 = 0, num2 = 0):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1+num2

# sum(4, 5)
# sum()

total = sum("a", 4)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

# multiple_items("Dave", "John", "Sara")
multiple_items([1, 9, 7])


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last="Gray")
