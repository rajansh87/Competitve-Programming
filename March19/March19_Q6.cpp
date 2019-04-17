#include<bits/stdc++.h>
using namespace std;
long long int formula(long long int arr[],long long int size,long long int p)
{
    long long int i,sum=0,j=1;
    for(i=p;i<size;i++)
    {
        sum=sum+(arr[i]/j);
        j++;
    }
    return sum;
}
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n,k;
        cin>>n>>k;
        long long int a[n],i,b[n]={0};
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }
        long long int l;
        long long int s=0,chef_pos=n-1;
        for(i=0;i<n;i++)
            {
                s=0;
                s=formula(a,n,i);
                if(s<=k)
                {
                    b[i]=1;
                }
                else
                {
                    b[i]=0;
                }
            }
        chef_pos=-1;
        i=0;
        while(b[i]!=1 && i<n)
        {
            chef_pos=i;
            i++;
        }
chef_pos=chef_pos+2;
cout<<chef_pos<<endl;
    }
return 0;
}
