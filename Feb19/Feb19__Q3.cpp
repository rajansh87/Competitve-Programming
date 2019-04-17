#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        int n;
        cin>>n;
        int a[n],d[n];
        int i;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }

        for(i=0;i<n;i++)
        {
            cin>>d[i];
        }
        int max1=-1;
        int p=0;
        for(i=0;i<n;i++)
        {
            p=a[(i-1)%n]+a[(i+1)%n];
            if(d[i]>p)
            {
                if(max1<d[i])
                {
                    max1=d[i];
                }
            }
        }
        if(max1>-1)
            cout<<max1<<endl;
        else
            cout<<"-1"<<endl;


        t--;
    }
return 0;
}
