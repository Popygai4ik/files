for i in range(200123, 200150+1):
    dele = []
    for z in range(1, i + 1):
        if i % z == 0:
            dele.append(z)
    if len(dele)== 4:
        print(i, '=', *dele)