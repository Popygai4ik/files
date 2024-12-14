def perevod_v_shesnatsetiresniu(shislo):
    s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if shislo < 16:
        return s[shislo]
    return perevod_v_shesnatsetiresniu(shislo // 16) + s[shislo % 16]


print(perevod_v_shesnatsetiresniu(int(input())))

