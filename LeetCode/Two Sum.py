# two sum problem with unsorted list and with duplicates allowed.
# link: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=set()
        s.add(nums[0])
        for i in nums[1::]:
            if target-i in s:
                i1,i2=nums.index(i),nums.index(target-i)
                if i1!=i2:
                    return [i1,i2]
                flag=0
                for j in range(len(nums)):
                    if nums[j]==target-i:
                        if flag==0:
                            flag=1
                            i1=j
                        else:
                            flag=0
                            i2=j
                            break
                return [i1,i2]
            s.add(i)
        return -1
        
