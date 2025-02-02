def find_special_numbers():
    result = []

    n = 800001
    while len(result) < 2:
        max_divisor_ending_with_3 = -1

        for d in range(4, n // 2 + 1):
            if n % d == 0 and d % 10 == 3:
                max_divisor_ending_with_3 = max(max_divisor_ending_with_3, d)


        if max_divisor_ending_with_3 != -1:
            result.append((n, max_divisor_ending_with_3))

        n += 1

    return result



special_numbers = find_special_numbers()

output = ''.join(f"{num}{div}" for num, div in special_numbers)

print(output)