'''
Arrays:
1. List ==> Built-in Data structure
  1. use [] to create a list
  2. List is mutable
  3. List is heterogenous
  4. List is indexed
  5. List is ordered
2. Array using array module
3. Array using numpy module
'''
'''
li = [1,12.5,True,1,"Python",2+5j]
print(li,type(li))

#No.of elements len()
print(len(li))

#update
li[2] = False
print(li)

#Adding element ==> append(),insert()
li.append(100)
print(li)

li.insert(1,100)
print(li)

li.insert(-20,300)
print(li)

li.insert(20,200)
print(li)

li.extend([300,400,500])
print(li)

#Removing element fromm the list
li.pop(2) #removes element by the index
print(li)

li.pop()  #removes the last element
print(li)

#li.pop(20)
#print(li) #index out of range ==> error

li.remove(100)
print(li) #removes the element to be remove without the index

li.clear()
print(li) #removes the whole list

#copy()
l1 = [1,2,3]
l2 = l1          #deep copy
l3 = l1.copy()   #shallow copy
print(l1,l2,l3)

l1.append(4)
print(l1,l2,l3)
'''
from array import array
arr = array('f',[10,20,30]) #'f' for float,'i' for integer
print(arr,type(arr))

arr.append(12.45)
