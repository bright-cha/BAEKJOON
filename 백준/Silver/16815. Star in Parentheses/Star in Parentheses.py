################내가 푼거 아님###########
def main():
    S = input()

    while '()' in S:
        S = S.replace('()', '')

    print(S.count('('))

if __name__ == '__main__':
    main()