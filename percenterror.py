while True:
    m = float(input("measured: "))
    e = float(input("expected: "))
    err = 100*((m - e) / e)
    print("percent error = " + str(err))
