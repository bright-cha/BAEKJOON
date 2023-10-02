R, G, B = map(int, input().split())
ans = 0

ans += R // 3
ans += G // 3
ans += B // 3

R %= 3
G %= 3
B %= 3

temp = [R, G, B]
while sum(temp) > 0:
    if temp.count(0) == 2:
        ans += 1
        break
    for i in range(3):
        if temp[i] > 0:
            temp[i] -= 1
    ans += 1

print(ans)
