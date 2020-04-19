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
#define loopvar(var,a,b) for(var=a;var<b;var++)
#define rloopvar(var,a,b) for(var=a;var>b;var--)
#define pb push_back
#define mp make_pair
int main()
{
    ll testcase=1;
    test
    {
        bool flag=true;
        int n,i,j;
        cin>>n;

        vector<pair<pair<int,int>,int> > arr(n);
        int a,b;
        loop1{
            cin>>a>>b;
            arr[i]={{a,b},i};
        }
        sort(arr.begin(),arr.end());

        vector<int> Cameron,Jamie; //Cameron and Jamie

        char ch,newArr[n];

        newArr[0]='C';

        loopi(1,n)
        {
            a=arr[i-1].first.first;
            b=arr[i-1].first.second;
            if(b>arr[i].first.first)
                {
                    ch=(newArr[i-1]=='C')?'J':'C';
                    while(i<n && b>arr[i].first.first)
                        {
                            newArr[i++]=ch;
                        }
                    i--;
                }
            else
            {
                newArr[i]=newArr[i-1];
            }
        }
        loop1
        {
            if(newArr[i]=='C')
                Cameron.pb(i);
            else
                Jamie.pb(i);
        }
        int cur=0,prev=0;
        if(Cameron.size()>0)
            prev=Cameron[0];
        loopi(1,Cameron.size())
        {
            cur=Cameron[i];
            if(arr[prev].first.second>arr[cur].first.first)
            {
                flag=false;
                break;
            }
            prev=cur;
        }
        if(flag)
        {
            if(Jamie.size()>0)
                prev=Jamie[0];
            loopi(1,Jamie.size())
            {
                cur=Jamie[i];
                if(arr[prev].first.second>arr[cur].first.first)
                {
                    flag=false;
                    break;
                }
                prev=cur;
            }
        }
        if(flag)
        {
            char ans[n];
            loopi(0,Cameron.size())
            {
                ans[arr[Cameron[i]].second]='C';
            }
            loopi(0,Jamie.size())
            {
                ans[arr[Jamie[i]].second]='J';
            }
            cout<<"Case #"<<testcase<<": ";
            loop1
            {
                cout<<ans[i];
            }
            cout<<endl;
        }
        else
        {
            cout<<"Case #"<<testcase<<": IMPOSSIBLE"<<endl;
        }

        //cout<<"Case #"<<testcase<<": "<<s<<" "<<mrow<<" "<<mcol<<endl;
        testcase++;

    }
    return 0;
}
