#include<bits/stdc++.h>
using namespace std;
int main()
{

long long n,k,q;
cin>>n>>k>>q;
long long int a[n],i,j,l=0,r=0,ans=0,startlimit=0,endlimit=0,c=0;
for(i=0;i<n;i++)
{
    cin>>a[i];
}
while(q--)
{
    cin>>l>>r;
    startlimit=min((l+ans)%n,(r+ans)%n);
    endlimit=max((l+ans)%n,(r+ans)%n);

    //startlimit=min(startlimit,endlimit);
    //endlimit=max(startlimit,endlimit);
    ans=0;
    c=0;
   // cout<<"start : "<<startlimit<<"\nend : "<<endlimit<<endl;
    for(i=startlimit;i<=endlimit;i++)
    {
        //c=count(a, a + endlimit, a[i]);
        for(j=startlimit+i;j<=endlimit;j++)
        {
            if(a[i]==a[j])
                c++;
        }
        if(c==k)
            ans++;
       // cout<<"c : "<<c<<endl;
        c=0;
    }

    cout<<ans<<endl;
}

//cout<<"ac : "<<(2%5)<<endl;
return 0;
}
