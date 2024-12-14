A = [3, 500, 35545545, 4, 5, 6]
for i in range(len(A)):
    A[i] = i
for i in range(len(A)):
    A[5 - i] = A[i]
print(A)