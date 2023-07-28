import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

rst = []
for a in nums:
    a_ = nums.pop(nums.index(a))
    for b in nums:
        b_ = nums.pop(nums.index(b))
        for c in nums:
            rst.append(a + b + c)
        nums.append(b_)
    nums.append(a_)

rst.sort(reverse=True)
for i in rst:
    if i <= m:
        print(i)
        break