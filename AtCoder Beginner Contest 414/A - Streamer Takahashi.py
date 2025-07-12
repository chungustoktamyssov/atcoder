n, l, r = [int(x) for x in input().split()]
count = 0

for i in range(n):
    x, y = [int(x) for x in input().split()]
    if x <= l and y >= r:
        count += 1

print(count)