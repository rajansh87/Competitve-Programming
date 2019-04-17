#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t>0)
    {
       long long int n,a,b,k,x,y,z,c;
       cin>>n>>a>>b>>k;
       c=a*b;
       x=n/a;
       y=n/b;
       z=n/c;
       long long int temp=x+y-2*z;

       if(__gcd(a,b)==1)
       {
           if(temp>=k)
           {
               cout<<"Win\n";
           }
           else
           {
               cout<<"Lose\n";
           }
       }
       if(__gcd(a,b)!=1)
       {
           if(x>y)
           {
               long long int ans=x+y-2*y;
               if(ans>=k)
               {
                    cout<<"Win\n";
               }
               else
               {
                    cout<<"Lose\n";
               }
           }
           else
           {
               long long int ans=x+y-2*x;
               if(ans>=k)
               {
                    cout<<"Win\n";
               }
               else
               {
                    cout<<"Lose\n";
               }
            }
        }

        t--;
    }
return 0;
}
