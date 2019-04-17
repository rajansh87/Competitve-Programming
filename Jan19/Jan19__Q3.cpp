#include<bits/stdc++.h>

using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int a[n],b[m];
    int i,j;

    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(i=0;i<m;i++)
    {
        cin>>b[i];
    }
    int c[m*n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            c[i+j]=a[i]+b[j];

        }
    }





    return 0;
}
