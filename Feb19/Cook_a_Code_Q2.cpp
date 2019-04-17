#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,a,b,ans1=1,ans2=1,num;
        cin>>n>>a>>b;
        if(a==1)
        {
            ans1=n;
        }
        else
        {
        for(i=0;i<a/2;i++)
        {
            ans1=ans1*(pow((n-i),2));
        }
        }

        if(b==1)
        {
            ans2=n;
        }
        else
        {
        for(i=0;i<b/2;i++)
        {
            ans2=ans2*pow((n-i),2);
        }
        }
        num=__gcd(ans1,ans2);
        //num=num-1;
        cout<<num<<endl;



    }

return 0;

}
