N = [i for i in range(1, int(input())+1)]
stack = []
while len(N) > 1:
    stack.append(N.pop(0))
    N.append(N.pop(0))
print(*stack, *N)