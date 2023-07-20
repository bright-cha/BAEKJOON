word = input()

word_numbers = [
    ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], 
    ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], 
    ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']
    ]

sec = 0
for word_number in word_numbers:
    for one_word in word:
        if one_word in word_number:
            sec += word_numbers.index(word_number)+3

print(sec)
