def a():
    print('a')
    def b():
        print('b')
    return b

a()