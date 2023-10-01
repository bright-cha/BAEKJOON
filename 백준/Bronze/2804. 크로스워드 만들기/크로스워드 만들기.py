A, B = input().split()
N, M = len(A), len(B)
matrix = [['.'] * N for _ in range(M)]

same = ''
idx1 = -1
idx2 = -1
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            same = A[i]
            idx1 = i
            idx2 = j
            break
    if idx1 != -1:
        break

for i in range(M):
    matrix[i][idx1] = B[i]

for i in range(N):
    matrix[idx2][i] = A[i]

for i in matrix:
    print(''.join(i))