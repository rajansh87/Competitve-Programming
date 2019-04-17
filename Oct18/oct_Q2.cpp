#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    long int T,p,N,i=0;
    cin>>T;
    while(T>0)
    {cin>>N;
    p=1;
    i=0;
    while(p<=N)
    {
        p=26*i;
        i++;
    }
    p=p-26;
    i=i-2;
    int q=N-p;
   // cout<<p<<endl<<i<<endl<<q;
    int nb=0,nn=0,nby=0;
    if(N<=2)
    {
        nb=1;
    }
    else if(q<2)
    {nb=pow(2,i);
   //cout<<endl<<"bits : "<<nb<<endl;
    }
    else if(q>=2&&q<=9)
    {
        nn=pow(2,i);
     //   cout<<endl<<"nibble : "<<nn<<endl;
    }
    else if(q>9)
        {
            nby=pow(2,i);
       //     cout<<endl<<"bytes : "<<nby<<endl;
        }
        cout<<nb<<" "<<nn<<" "<<nby<<endl;
        T--;
    }
    return 0;
}
