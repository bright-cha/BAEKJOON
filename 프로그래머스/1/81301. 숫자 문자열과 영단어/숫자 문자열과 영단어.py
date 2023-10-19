def solution(s):
    eng_num = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
    }
    
    ans = ''
    temp = ''
    for i in s:
        try:
            i = int(i)
            ans += str(i)
        except:
            temp += i
            if temp in eng_num:
                ans += eng_num[temp]
                temp = ''
            
    answer = int(ans)
    return answer