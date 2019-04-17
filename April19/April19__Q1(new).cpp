#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,i,a,n1=0,n2=0;
    cin>>n;
    cin>>n2;
    for(i=1;i<n;i++)
    {
        cin>>a;
       // if(i==0)
        //    n2=a;
        if(n2<a)
        {
            n1=n2;
            n2=a;
        }
    }
    cout<<n1<<endl;
    return 0;
}
