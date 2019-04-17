#include<bits/stdc++.h>
using namespace std;
int main()
{
  long t,n;
  cin>>t;
  for(long j=0;j<t;j++)
 {
    cin>>n;
    for(long i=0;i<=n/26;++i)
     {
        if(0<n && n<=2)
            {cout<<1<<" "<<0<<" "<<0<<"\n";
              break;}
        else if(2<n && n<=10)
            {cout<<0<<" "<<1<<" " <<0<<"\n";
             break;}
        else if(10<n&& n<=26)
            {cout<<0<<" "<<0<<" "<<1<<"\n";
                 break;}
        long long k=pow(2,i);
        if(26*i<n && n<=26*i+2)
            {cout<<k<<" "<<0<<" "<<0<<"\n";
            break;}
        else if(26*i+2<n && n<=26*i+10)
     {cout<<0<<" "<<k<<" "<<0<<"\n";
       break;}
    else if(26*i+10<n && n<=26*(i+1))
      {cout<<0<<" "<<0<<" "<<k<<"\n";
        break;}
     }
 }
 return 0;
}
