student = int(input())
nums = list(map(int, input().split()))

rst = []
for i in range(len(nums)):
    rst.insert(nums[i], i+1)

rst.reverse()
print(*rst)