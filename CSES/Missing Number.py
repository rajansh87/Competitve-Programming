# given a list containing elements from 1 to n. find the missing number.
# link: https://cses.fi/problemset/task/1083/

n=int(input())
arr=list(map(int,input().split()))
print(n*(n+1)//2-sum(arr))
