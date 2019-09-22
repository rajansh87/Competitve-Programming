#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int d,i,loc,n1,sum=0;
        cin>>d;
        float ans,c;
        string s;
        cin>>s;
        n1=count(s.begin(),s.end(),'A');
        if(n1==d)
            cout<<-1<<endl;
        else{
        loc=count(s.begin(),s.end(),'P');
        c=loc;
        for(i=2;i<d-2;i++)
        {

            if(s[i]=='A' && ((c/d)*100)<75)
            {
                if((s[i-1]=='P' || s[i-2]=='P')&& (s[i+1]=='P' || s[i+2]=='P'))
                {
                    c++;
                    sum++;
                }
            }
            ans=(c/d)*100;
            if(ans>=75)
                break;
        }
        ans=(c/d)*100;
        if(ans>=75)
            cout<<sum<<endl;
        else
            cout<<-1<<endl;
    }
    }

    return 0;
}
