# link: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calcArea(firstLength: int, secLength: int, firstBreadth: int, secBreadth: int) -> int:
            l=min(firstLength,secLength)
            b=secBreadth-firstBreadth
            area=l*b
            return area
        
        allAreas=[]
        low,high=0,len(height)-1
        while low<high:
            area=calcArea(height[low],height[high],low,high)
            allAreas.append(area)
            if height[low]>height[high]:
                high-=1
            else:
                low+=1
            
        return(max(allAreas))
        
        
