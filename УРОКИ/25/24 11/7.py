for i in range(600001, 600001 +1000):
    for z in range(17, i, 10):
        if i % z == 0:
            print(i, z)
            break