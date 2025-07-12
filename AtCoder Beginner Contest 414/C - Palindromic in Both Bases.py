# this tle idk why its o(sqrt(n) * log(n)) --> im a pig

a = int(input())
n = int(input())
ans = 0

def base_a(s, a):
    converted_num = ''

    quotient = 1
    while quotient != 0:
        quotient = s//a
        remainder = s % a
        s = quotient
        
        converted_num += str(remainder)
    converted_num = converted_num[::-1]

    return converted_num

def palindrome(s):
    global ans

    actual_s1 = int(s+s[::-1])
    actual_s2 = int(s)
    if len(s) > 1:
        actual_s2 = int(s + s[-2::-1])

    if actual_s1 <= n:
        converted_s = base_a(actual_s1, a)
        if converted_s == converted_s[::-1]:
            ans += actual_s1  
    if actual_s2 <= n:
        converted_s = base_a(actual_s2, a)
        if converted_s == converted_s[::-1]:
            ans += actual_s2

    if actual_s1 > n or actual_s2 > n:
        return None

    for i in range(1, 10):
        palindrome(s+str(i))

for i in range(1, 10):
    palindrome(str(i))

print(ans)