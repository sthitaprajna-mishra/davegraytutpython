name = "Dave"
count = 1

def another():
    # count += 1
    global count
    count += 1

    color = "blue"

    def greeting():
        print(count)

        nonlocal color

        color = "red"
        print(color)
        print(name)

    greeting()

another()