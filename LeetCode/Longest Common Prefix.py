# link: https://leetcode.com/problems/longest-common-prefix/

class Solution:
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
                
        
        
