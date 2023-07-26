n = int(input())
ch = {input(): i for i in range(n)}

if ch['KBS1'] != 0:
    for i in range(ch['KBS1']):
        print(1, end='')
    for i in range(ch['KBS1']):
        print(4, end='')
        ch['KBS1'] -= 1    
        if ch['KBS1'] == ch['KBS2']:
            ch['KBS2'] += 1

if ch['KBS2'] != 1:
    for i in range(ch['KBS2']):
        print(1, end='')
    for i in range(ch['KBS2'] - 1):
        print(4, end='')    
        ch['KBS2'] -= 1