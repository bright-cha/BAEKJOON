N = int(input())
P = input().split('*')

for _ in range(N):
    fileName = input()
    ans = True

    if not P[0] == fileName[:len(P[0])]:
        ans = False

    if not fileName[len(P[0]):].endswith(P[1]):
        ans = False

    if ans:
        print('DA')
    else:
        print('NE')
