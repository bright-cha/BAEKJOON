n = int(input())
result = 0

for i in range(n):
    word_list = set()
    word = input()
    
    for j in range(len(word) - 1):
        if word[j] != word[j + 1] :
            if word[j + 1] in word_list:
                break
            if word[j] not in word_list:
                word_list.add(word[j])

    else:
        result += 1

print(result)