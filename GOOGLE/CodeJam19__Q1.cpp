#include<bits/stdc++.h>
using namespace std;
int checkNum(int num)
{
    int i,r;
    while(num>0)
    {
        r=num%10;
        num=num/10;
        if(r==4)
            return 1;
    }
        return 2;
}
int main()
{
    int t,count=1;
    cin>>t;
    while(t--)
    {
        int n,a,b,p=0,q=0,c=0;
        cin>>n;
        if(n%2==0)
        {
            a=n/2;
            b=n/2;
        while(c<n/2)
        {
            p=checkNum(a);
            q=checkNum(b);
            if(p==2 && q==2)
            {
                if(a+b==n)
                    {
                        cout<<"Case #"<<count<<": "<<a<<" "<<b<<endl;
                        break;
                    }
                    else
                    {
                        a--;
                        b++;
                    }
            }
            else
                    {
                        a--;
                        b++;
                    }
            c++;
        }
    }
            else
                {
                    a=n/2;
                    b=n/2+1;
        while(c<n/2)
        {
            p=checkNum(a);
            q=checkNum(b);
            if(p==2 && q==2)
            {
                if(a+b==n)
                    {
                        cout<<"Case #"<<count<<": "<<a<<" "<<b<<endl;
                        break;
                    }
                    else
                    {
                        a--;
                        b++;
                    }
            }
            else
                    {
                        a--;
                        b++;
                    }
            c++;
        }
                }
            count++;
    }
return 0;
}
