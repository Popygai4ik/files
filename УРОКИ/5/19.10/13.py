def to_base_13(n):
    """Convert a decimal number to base 13."""
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % 13))
        n //= 13
    return ''.join(str(x) for x in digits[::-1])


def from_base_13(s):
    """Convert a base 13 number (as string) to decimal."""
    return sum(int(digit) * (13 ** i) for i, digit in enumerate(reversed(s)))


def process_number(n):
    """Process the number according to the algorithm."""
    base_13_str = to_base_13(n)

    last_digit = int(base_13_str[-1])

    if last_digit % 2 == 0:  # Even
        modified_str = base_13_str[:-2] + "1A" + base_13_str[-1] + "B"
    else:  # Odd
        modified_str = base_13_str[:-2] + "21" + base_13_str[-1] + "A"

    return from_base_13(modified_str)


# Find the minimum R greater than 862
min_r = None
n = 1

while True:
    r = process_number(n)
    if r > 862:
        min_r = r
        break
    n += 1

print(min_r)
