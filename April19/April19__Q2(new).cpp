#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
    long long int n,i,j;
    string str;
    char ch;
    cin>>n;
    cin>>str;
    cin>>ch;
    long long p=n*(n+1)/2;
    for(i=0;i<n;i++)
    {
        for(j=i;j<n;j++)
        {
            if(str[j]!=ch)
                {
                    p--;
                }
            else
                {
                    break;
                }
        }
    }
    cout<<p<<endl;

   }
    return 0;
}

