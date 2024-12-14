def is_special_number(num):
    """Check if a number is a special number according to the problem."""
    if num >= 0:
        return False
    num_base7 = ''
    num_abs = abs(num)
    while num_abs > 0:
        num_base7 = str(num_abs % 7) + num_base7
        num_abs //= 7
    return num_base7.startswith('3')


def max_sum_subsequence(numbers, K):
    N = len(numbers)
    max_sum = float('-inf')

    for start in range(N):
        special_count = 0
        current_sum = 0

        for end in range(start, N):
            current_sum += numbers[end]
            if is_special_number(numbers[end]):
                special_count += 1

            if special_count % K == 0:
                max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    with open('1.txt', 'r') as file:
        first_line = file.readline().strip().split()
        N = int(first_line[0])
        K = int(first_line[1])
        numbers = [int(file.readline().strip()) for _ in range(N)]

    result = max_sum_subsequence(numbers, K)
    print(result)


if __name__ == "__main__":
    main()
