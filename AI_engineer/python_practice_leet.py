n=[4,3,2,7,8,2,3,1] ## o [5,6]
#n= [1,1]
def findDisappearedNumbers_1(n):
    l=[]
    for i in range(1,len(n)+1):
        if i not in n:
            l.append(i)
    return l 

## not suitable for larger sets
print(findDisappearedNumbers_1(n))

# visiting every room in a hotel 
#inplace marking 

def findDisappearedNumbers(nums) :
    # Mark existing numbers by making the value at their index negative
    for n in nums:
        index = abs(n) - 1
        nums[index] = -abs(nums[index])
        
    # If a number at index i is positive, i+1 never appeared
    return [i + 1 for i, num in enumerate(nums) if num > 0]


print(findDisappearedNumbers(n))

nums = [0,1,0,3,12]

def movezeros_1(nums):
    l,r,temp =0,1,0
    for i in range(len(nums)):
        if nums[l]==0 and r<len(nums):
            print(nums[l],nums[r])
            if nums[r]==0:
                r +=1
            else:
                temp = nums[r]
                nums[r]= nums[l]
                nums[l]=temp
                l +=1
                r +=1
        else:
            l +=1
            r +=1
    return nums

def moveZeroes(nums) -> None:
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums
    
    # Note: The problem asks for "in-place" modification, 
    # so we don't usually return anything (it modifies nums directly). 

print(movezeros_1(nums))

print(moveZeroes(nums))


##design order streams 

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]* (n+1)
        self.ptr =1
        
    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        chunk =[]
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1
        return chunk

## ["OrderedStream","insert","insert","insert","insert","insert"]
## [[5],[3,"ccccc"],[1,"aaaaa"],[2,"bbbbb"],[5,"eeeee"],[4,"ddddd"]]

#Output
#[null,[],["aaaaa"],["bbbbb","ccccc"],[],["ddddd","eeeee"]]

import numpy as np 
#Left and Right Sum Differences
nums = [10,4,8,3]
def leftRightDifference(nums):
    l1,r1=[],[]
    l_sum,r_sum =0,0
    l,r =0,len(nums)-1
    for i in range(len(nums)):
        if l <len(nums):
            l1.append(l_sum)
            l_sum = l_sum+nums[l]
            l +=1
            r1.append(r_sum)
            r_sum = r_sum+nums[r]
            r -=1
    return np.abs(np.array(l1) - np.array(r1[::-1])).tolist()

print(leftRightDifference(nums))

from typing import List

class Solution:
    # Now this will work
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        #print(res)
        for i in range(n - 2):
            for j in range(n - 2):
                current_max = 0
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        #print(current_max,grid[row][col])
                        current_max = max(current_max, grid[row][col])
                res[i][j] = current_max
                
        return res

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Create the object AND call the function with the grid
print(Solution().largestLocal(grid))

