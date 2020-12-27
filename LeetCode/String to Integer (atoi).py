# Print the integer value by removing whitespaces and if string in starting then its wrong.
# link: https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.strip()
        a=""
        if s=="":                 
            return 0
        if s[0] == "-":           
            a+="-"
            s=s[1:]
        else:
            if s[0] == "+":
                s=s[1:]
        for i in s:
            if(i.isdigit()):
                a+=i   
            else:
                break
        if a=="" or a=="-":
            a+="0" 
        if (int(a)<= - 2**31):
            return -2**31
        elif (int(a)>= 2**31 -1):
            return 2**31 -1
        else:
            return int(a) 
                
                
        
