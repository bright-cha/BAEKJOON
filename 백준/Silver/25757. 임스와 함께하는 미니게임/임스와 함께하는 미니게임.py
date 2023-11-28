import sys
input = sys.stdin.readline

N, kind_of_game = input().rstrip().split()
N = int(N)
people = set([input().rstrip() for _ in range(N)])

if kind_of_game == 'Y':
    print(len(people))
elif kind_of_game == 'F':
    print(len(people) // 2)
else:
    print(len(people) // 3)