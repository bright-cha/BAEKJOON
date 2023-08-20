N = int(input())
for i in range(1, N+1):
    string = list(input().split())

    if len(string) > 1:
        string.reverse()
        print(f'Case #{i}:', *string)
    else:
        print(f'Case #{i}:', ''.join(string))