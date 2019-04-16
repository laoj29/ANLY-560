if __name__ == '__main__':
    a = 'first variable'
    b = 'second variable'
    b, a = a, b
    print("a: %s" % a)
    print("b: %s" % b)