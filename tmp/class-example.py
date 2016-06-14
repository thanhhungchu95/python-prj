def first():
    def hi():
        hi = "Hi world!"

    def goodbye():
        nonlocal goodbye
        goodbye = "Goodbye World!"

    def hello():
        global hello
        hello = "Hello World!"

    hi()
    print("Say:", hi)
    goodbye()
    print("Say:", goodbye)
    hello()
    print("Say:", hello)

first()
