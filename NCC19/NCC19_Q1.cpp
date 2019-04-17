#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long long int n,k,i;
        cin>>n>>k;
        long long int a[k];
        for(i=0;i<k;i++)
            {
                cin>>a[i];
            }
        long long int sum=0;
        i=0;
        long long int count=0;
        for(i=0;i<k;i++)
        {
            sum=sum+a[i];
            if(sum<=n)
            {
                count++;
            }
        }
        cout<<(count)<<endl;;
    }

return 0;
}
