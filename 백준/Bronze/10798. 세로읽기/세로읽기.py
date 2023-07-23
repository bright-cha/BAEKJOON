words = []
len_w = []

for i in range(5):
    words.append(list(input()))
    len_w.append(len(words[i]))


for j in range(max(len_w)):
    for i in range(5):
        try:
            print(words[i][j], end = '')
        except:
            continue