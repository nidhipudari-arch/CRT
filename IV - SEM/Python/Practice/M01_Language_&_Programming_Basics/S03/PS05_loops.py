'''
n = int(input())
count = 0
while n>0:
    count+=1
    n//=10
print(count)

for count in range(0,5,1):
    print("Hello World")

li = [ 1,2,3,4,5]
for i in range(len(li)):
    li[i] = li[i]**2
print(li)

li = [1,2,3,4,5]
for i in range(len(li)):
    if li[i] % 2 == 0:
        print(li[i],end=" ")

for ele in li:
    if ele % 2 == 0:
        print(ele,end =" ")

n = input()
count = 0
for ch in n:
    if ch in 'aeiouAEIOU':
        count +=1 
print(count)

for i in range(1,11):
    if i == 5:
        continue
    print(i,end=" ")
'''
password = "abc123"
attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Password matched")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Access denied")

