
//NCC1902

#include<bits/stdc++.h>
using namespace std;
int digisum(long long int a)
{
    long long int b,sum=0;
    if(a<10)
        return a;
    else
    {
        b=a;
        while(b>0)
        {
            sum=sum+b%10;
            b=b/10;
        }
        return digisum(sum);
    }
}
int main()
{
    int q;
    cin>>q;
    while(q--)
    {
        long long int l,r,n1,n2;
        cin>>l>>r>>n1>>n2;
        long long int countn1=0,countn2=0;

            long long int i,p;
            for(i=l;i<=r;i++)
            {
                p=digisum(i);
                if(n1==p)
                    countn1++;
                if(n2==p)
                    countn2++;
            }


        if(countn1==countn2)
            cout<<"Draw\n";
        else if(countn1>countn2)
            cout<<"Onkar\n";
        else
            cout<<"Krushna\n";
    }

return 0;
}
