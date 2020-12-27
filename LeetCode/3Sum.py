# Print all triplets whose sum is equal to zero in a array.
# link: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        target=0
        ans=[]
        for i in range(len(arr)-2):
            num1=arr[i]
            s=set()
            j=i+1
            s.add(arr[j])
            for k in arr[j+1::]:
                if target-num1-k in s:
                    ans.append([num1,target-num1-k,k])
                else:
                    s.add(k)
        a=[]
        for i in ans:
            if sorted(i) not in a:
                a.append(sorted(i))
        return a
