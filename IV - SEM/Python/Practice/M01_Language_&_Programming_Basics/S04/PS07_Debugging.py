'''
import random
li = [1,2,3]
i = random.randint(0,3)
print(i,li[i])
'''
li = list(map(int, input().split()))

i = len(li) - 1
while i >= 0:
    if li[i] < 9:
        li[i] += 1
        break
    else:
        li[i] = 0
        i -= 1

if i < 0:
    li.insert(0, 1)

print(li)
1
