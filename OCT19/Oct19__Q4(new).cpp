#include<bits/stdc++.h>
#include <vector>
#include <cmath>
#define ll long long int
#define loop1 for(i=0;i<n;i++)
#define loop2 for(j=0;j<n;j++)
#define loopi(a,b) for(i=a;i<b;i++)
#define loopj(a,b) for(j=a;j<b;j++)
#define rloopi(a,b) for(i=a;i>b;i--)
#define rloopj(a,b) for(j=a;j>b;j--)
#define test long long int t;cin>>t;while(t--)
using namespace std;
int main()
{
    test
    {
        ll n;
        cin>>n;
        vector<ll>arr(n);
        ll i,j;
        loop1
            {
                cin>>arr[i];
            }

        vector<ll>x(1000005,0);
        ll mx=0;
        loop1
            {
                if(mx<x[arr[i]])
                {
                    mx=x[arr[i]];
                }
                for(j=1;j<=sqrt(arr[i]);j++)
                {
                    if(arr[i]%j==0)
                    {
                        if((arr[i]/j)==j)
                        {
                            x[j]++;
                        }
                        else
                        {
                            x[arr[i]/j]++;
                            x[j]++;
                        }
                    }
                }
            }
            cout<<mx<<endl;
        }
    return 0;
}

