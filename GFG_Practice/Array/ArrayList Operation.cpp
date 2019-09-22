#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define loop1 for(i=0;i<n;i++)
#define loop2 for(j=0;j<n;j++)
#define loopi(a,b) for(i=a;i<b;i++)
#define loopj(a,b) for(j=a;j<b;j++)
#define rloopi(a,b) for(i=a;i>b;i--)
#define rloopj(a,b) for(j=a;j>b;j--)
#define test long long int t;cin>>t;while(t--)
int main()
{
   test
   {
        ll q,i,j,freq=0;
        char a,b;
        string s="";
        cin>>q;
        while(q--)
        {
            cin>>a>>b;
            if(a=='i')
            {
                s=s+b;
            }
            else if(a=='f')
            {
                freq=count(s.begin(),s.end(),b);
            }
        }
        if(freq!=0)
            cout<<freq<<endl;
        else
            cout<<"Not Present"<<end;


   }
    return 0;
}

