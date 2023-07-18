students = set()
submiter = set()

for i in range(1, 31):
    students.add(i)

for __ in range(28):
    submiter.add(int(input()))

unsubmit = students - submiter
list_unsubmit = list(unsubmit)
list_unsubmit.sort()

print(list_unsubmit[0])
print(list_unsubmit[1])