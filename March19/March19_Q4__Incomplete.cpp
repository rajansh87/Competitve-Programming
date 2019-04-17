#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        int a[n],i,j;
        for(i=0;i<n;i++)
            cin>>a[i];


        int count=0,l,arr[2*n];
        count=count+n;
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                for(l=1;l<=k;l++)
                {
                    for(m=0;m<n;m++)
                    {
                        a[l+m]=a[i];
                        a[l+m+1]=
                    }
                }
            }
        }




	}
	return 0;
}
