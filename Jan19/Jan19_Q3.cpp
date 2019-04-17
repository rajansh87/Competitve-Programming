#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int a[n],b[m];
    int i,j,c=1,k,l;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(i=0;i<m;i++)
    {
        cin>>b[i];
    }
    int s[n][m];
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            s[i][j]=a[i]+b[j];
        }
    }
    int z=0;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            c=0;
            for(k=0;k<n;k++)
            {
                for(l=0;l<m;l++)
                {
                    if(s[i][j]==s[k][l])
                        c++;
                }
            }

            if(c==1)
            {if(z<(n+m-1)){
                cout<<i<<" "<<j<<endl;}
                z++;}
        }
    }



    /*for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            cout<<s[i][j]<<" ";
        }
        cout<<endl;
    }*/

return 0;
}
