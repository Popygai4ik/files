c = 0
def check_array(arr):
    for i in range(len(arr) - 1):
        if (arr[i] % 2 == 0 and arr[i + 1] % 2 == 0) or \
            (arr[i] % 2 != 0 and arr[i + 1] % 2 != 0):
            return False
    return True
for i in range(100_000, 100_0000):
    sh = oct(i)[2:]
    # print(sh)
    if check_array([int(i) for i in sh]):
        c += 1

print(c)