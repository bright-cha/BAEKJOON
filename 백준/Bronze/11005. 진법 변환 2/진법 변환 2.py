import string

def convert_recur(num, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    return convert_recur(q, base) + number[r] if q else number[r]


num, base = map(int, input().split())


print(convert_recur(num, base))