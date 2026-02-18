'''
1) write a python code for the factorial of a number?

n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
    print(fact)'''
'''
2)write a code to check whether the number is armstrong or not? 
'''
'''
n = int(input())
d = len(str(n))
print("Armstrong" if sum(int(i)**d for i in str(n)) == n else "Not Armstrong")'''
'''
prime or not
n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")'''
'''
prime numbers with a range
n = int(input("Enter start: "))
m = int(input("Enter end: "))

for num in range(n, m + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")'''
'''
a = list(map(int,input().split()))
if a == sorted(a) or a == sorted(a,reverse = True):
    print("Monotonic")
else:
    print("Not Monotonic")
x = int(input())
sign = 1
if x < 0:
    sign = -1
    x = -x
rev = 0
while x > 0:
    digit = x % 10
    rev = rev * 10+digit
    x = x // 10
rev = rev * sign
if rev < - 2**31 or rev > 2**31-1:
    print(0)
else:
    print("Reversed Integer:",rev)
s = input().upper()
d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

res = 0
for i in range(len(s)):
    if i+1 < len(s) and d[s[i]] < d[s[i+1]]:
        res -= d[s[i]]
    else:
        res += d[s[i]]

print(res)'''
n = int(input())
seen = set()
while n!= 1 and n not in seen:
    seen.add(n)
    sum_sq = 0
    while n > 0:
        digit = n%10
        sum_sq += digit * digit
        n = n // 10
    n = sum_sq
if n == 1:
    print("Happy Number")
else:
    print("Not Happy Number")








