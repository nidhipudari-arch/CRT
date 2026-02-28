'''def running_sum (nums):
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums
print(running_sum([1,2,3,4]))
print(running_sum([3,1,2,10,1]))
#contains duplicates
def contains_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
print(contains_duplicate([1,2,1,3,4,1,5,1,2,3,4,5]))
def maximumWealth(accounts):
    max_wealth = 0
    
    for customer in accounts:
        wealth = sum(customer)   
        if wealth > max_wealth:
            max_wealth = wealth
    
    return max_wealth
print(maximumWealth([[1,2,3],[3,2,1]]))
print(maximumWealth([[1,5],[7,3],[3,5]]))
#concatination of arrays
def getConcatenation(nums):
    return nums + nums
print(getConcatenation([1,2,3])) #either nums+nums or nums*2
def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result
print(shuffle([2,5,1,3,4,7], 3))
t = (10,23)
t[1] = 50 #error
print(t)
t = (10,23,50,21,44,65)
t2 = ("sai", "preeti", "priya")

print(t[0])
print(t[-1])
print(t + t2)
print(t,t2)
print(t*5)
print(t[1:4])
print(t[:5])
print(t[:-1])
del t
#to print intersection of arrays 
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    res = (set1 & set2)
    return tuple(res)
print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and \
               moves.count('L') == moves.count('R')
print(Solution().judgeCircle("UD"))
print(Solution().judgeCircle("LL"))
moves = "UDLR"

position = (0, 0)   # (x, y)

for move in moves:
    x, y = position
    
    if move == 'U':
        position = (x, y + 1)
    elif move == 'D':
        position = (x, y - 1)
    elif move == 'R':
        position = (x + 1, y)
    elif move == 'L':
        position = (x - 1, y)

if position == (0, 0):
    print(True)
else:
    print(False)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = (0,0)
        x,y = position
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x += 1
            elif move == 'R':
                x -= 1
        position = (x , y)
        return position == (0,0)
d = {"a":'Sreenidhi'}
print(d)
d2 = dict(a='Sreenidhi', b = 'Preeti', c = 'Priya')
print(d2)
print(d2['a'])
print(d2.get('b'))
print(d2.keys())
print(d2.values())'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[nums[i]] = i