#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int i,j,p[n],b[n];
    for(i=0;i<n;i++)
    {
        cin>>p[i]>>b[i];
    }
    for(i=0;i<n;i++)
    {
        if(b[i]>m)
        {
            b[i]=0;
            p[i]=0;
        }
    }

    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(b[i]==b[j])
            {
                if(p[i]>p[j])
                {
                    b[j]=0;
                    p[j]=0;
                }
                else
                {
                    b[i]=0;
                    p[i]=0;
                }
            }
        }
    }
int sum=0;
    for(i=0;i<n;i++)
    {
        sum=sum+p[i];
    }
    cout<<sum<<endl;





return 0;
}
