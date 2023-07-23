title = []
point = []
rank = []
score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for __ in range(20):
    t, p, r =  input().split()
    if r == 'P':
        continue
    title.append(t)
    point.append(float(p))
    rank.append(score[r])
jihun = list(map(lambda t, p, r: {'title':t, 'score': p * r}, title, point, rank))

result = sum([total['score'] for total in jihun])

print(f'{result / sum(point): .6f}')