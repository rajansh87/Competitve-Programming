#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int T;
    cin>>T;
    while(T--)
    {
        long long int N,Z;
        cin>>N>>Z;
        long long int arr[N],j,v,p=0,q=0,r=0;
        for(j=0;j<N;j++)
            {
                cin>>arr[j];
            }
        while(Z--)
        {
            for(j=0;j<N;j++)
            {
                if((arr[j]==0 && arr[j+1]==1))
                {
                    v=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=v;
                    j++;
                }
            }
        }
        for(j=0;j<N;j++)
            {
                cout<<arr[j]<<" ";
            }
        cout<<"\n";
    }
return 0;
}
