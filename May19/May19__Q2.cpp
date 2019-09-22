#include<bits/stdc++.h>
using namespace std;
int main()
{
long long int t;
 cin>>t;
 while(t--)
 {
  long long int m,n,a,b,c=0,f=0;
   cin>>m>>n;
     if(m%n==0 || m/n>1)
     {
     cout<<"Ari"<<endl;
     continue;
     }

       while(true)
       {
          a=max(m,n);
          b=min(m,n);
          if( a%b==0 || a/b>1)
          {
                    if(f==0)            //0 is for ari and 1 is for rich
                        cout<<"Ari"<<endl;
                    else
                        cout<<"Rich"<<endl;
                    break;
          }
          if(f==0)
            f=1;        //for each turn
          else f=0;
          m=a%b;
          n=b;
        //  cout<<m<<" "<<n<<"due to:  "<<f<<endl;
       }
 }
}
