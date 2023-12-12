import sys
input = sys.stdin.readline

def search(DNA):
    count = 0
    standard = 0
    A, C, G, T = DNA

    CA, CC, CG, CT = word[:p].count('A'), word[:p].count('C'), word[:p].count('G'), word[:p].count('T')

    while standard <= s - p:
        if A <= CA and C <= CC and G <= CG and T <= CT:
            count += 1

        # 기존 시작지점 갯수 감소
        if word[standard] == 'A':
            CA -= 1
        elif word[standard] == 'C':
            CC -= 1
        elif word[standard] == 'G':
            CG -= 1
        elif word[standard] == 'T':
            CT -= 1

        # 새로운 시작지점 갯수 증가
        if standard + 1 <= s - p:
            if word[standard + p] == 'A':
                CA += 1
            elif word[standard + p] == 'C':
                CC += 1
            elif word[standard + p] == 'G':
                CG += 1
            elif word[standard + p] == 'T':
                CT += 1

        standard += 1

    return count


s, p = map(int, input().split())
word = input().rstrip()
DNA = list(map(int, input().split()))

print(search(DNA))