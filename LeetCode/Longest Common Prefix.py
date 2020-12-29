# link: https://leetcode.com/problems/longest-common-prefix/

class Solution:                       #normal approach
    def longestCommonPrefix(self, strs: List[str]) -> str:            
        if len(strs)==0:
            return ""
        if strs==[strs[0]]*len(strs):
            return strs[0]
        strs.sort(reverse=True)
        word=strs[0]
        prefixes=[]
        for i in range(1,len(word)+1):
            s=word[:i]
            prefixes.append(s)
        dic=dict()
        for i in prefixes:
            dic[i]=1
        for i in range(1,len(strs)):
            for j in prefixes[::-1]:
                word=strs[i]
                word_prefixes=[]
                for k in range(1,len(word)+1):
                    s=word[:k]
                    word_prefixes.append(s)
                if j in word_prefixes:
                    dic[j]+=1
        
        maxCount=max(dic.values())
        if maxCount!=len(strs):
            return ""
        word,l="",0
        for key,val in dic.items():
            if val==maxCount:
                if len(key)>l:
                    l=len(key)
                    word=key
        
        return word
                
########
class Solution:                     # efficient approach using Binary search concept
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isCommonPrefix(strs: List[str], le: int) -> bool:
            str1=strs[0][:le]
            for i in range(1,len(strs)):
                if not strs[i].startswith(str1):
                    return False
            return True
        
        if strs=="" or len(strs)==0:
            return ""
        minLen=1000000000000
        for st in strs:
            minLen=min(minLen,len(st))
        low=1
        high=minLen
        while low<=high:
            mid=(low+high)//2
            if isCommonPrefix(strs,mid):
                low=mid+1
            else:
                high=mid-1
        return strs[0][:(low+high)//2]
    
        
        
