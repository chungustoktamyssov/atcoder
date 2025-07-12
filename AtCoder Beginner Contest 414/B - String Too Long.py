n = int(input())
s = ''
tooLong = False

for i in range(n):
    c, l = input().split()
    l = int(l)

    if tooLong: pass
    else:
        if l + len(s) > 100:
            tooLong = True
        else:
            s += c * l

if tooLong:
    print('Too Long')
else:
    print(s)