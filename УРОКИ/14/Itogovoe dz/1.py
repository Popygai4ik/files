s= 59**361 + 61**539 - 39**651 - 361
bin_n = bin(s)[2:].count('1')
print(oct(bin_n))