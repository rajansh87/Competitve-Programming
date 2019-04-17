#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n;
        cin>>n;
        long long int a[n],i;
        for(i=0;i<n;i++)
            cin>>a[i];

        sort(a,a+n);
        long long int sum=0,c2=0,s=0,count=0,c=0;
        i=0;
        for(i=0;i<n;i++)
        {
            if(a[i]==0)
            c2++;
        }
        if(c2==n)
            {
                cout<<"0"<<" "<<"0"<<endl;
            }
        else{
        for(i=0;i<n;i++)
        {
            if(a[i]>0)
            {
                sum=sum+a[i];
                count++;
            }
            else
            {
                s=s+a[i];
                c++;
            }
        }
        s=pow(s,2);
        sum=pow(sum,2);
        if(sum>s)
        {
            if(count==n)
                cout<<count<<" "<<count<<endl;
            else
                cout<<count<<" "<<c<<endl;
        }
        else if(sum<s)
        {
            if(c==n)
                cout<<c<<" "<<c<<endl;
            else
                cout<<c<<" "<<count<<endl;
        }
        else if(sum==s)
        {
            if(count>c)
                cout<<count<<" "<<c<<endl;
            else
                cout<<c<<" "<<count<<endl;
        }
        }

    }


return 0;
}
