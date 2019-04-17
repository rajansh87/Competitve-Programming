#include<bits/stdc++.h>
using namespace std;
//#define sol ((((n%i)%j)%k)%n)
int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        long long int n=0,p,i=1,j=1,k=1,var1=0,var2=0;
        cin>>n>>p;
        long long int m=0;
       /* for(i=1;i<=p;i++)
        {
            for(j=1;j<=p;j++)
            {
                for(k=1;k<=p;k++)
                {
                    var1=sol;
                     if(var1==1)
                        {
                            m++;
                            //cout<<i<<":"<<j<<":"<<k<<endl;
                        }
                }
            }
        }*/

        if(n<3)
        {
            cout<<(p*p*p)<<endl;
        }/*
        else if(n==2)
        {
            cout<<pow(p,3)<<endl;
            continue;
        }*/
        else
        {
        var1=0;

        var1+=(p-(n-1)/2)*(p-(n-1)/2);
        var1+=(p-n)*(p-(n-1)/2);
        var1+=(p-n)*(p-n);
        cout<<var1<<endl;
        }
        /*else{
       for(i=1;i<=p;i++)
        {
            for(j=1;j<=p;j++)
            {
                for(k=1;k<=p;k++)
                {
                    var1=sol;
                     if(var1>var2)
                        {
                            var2=var1;
                            //cout<<i<<":"<<j<<":"<<k<<endl;
                        }
                }
            }
        }
        m=0;
        for(i=1;i<=p;i++)
        {
            for(j=1;j<=p;j++)
            {
                for(k=1;k<=p;k++)
                {
                    var1=sol;
                     if(var1==var2)
                        {
                            m++;
                            cout<<i<<":"<<j<<":"<<k<<"  ";
                        }
                }
            }
        }
        }*/
//cout<<endl<<m<<endl;
        t--;
    }
return 0;
}
