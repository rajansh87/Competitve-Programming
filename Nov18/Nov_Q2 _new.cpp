#include<iostream>
#include<stdlib.h>
#include <algorithm>
using namespace std;
int main()
{
    long int t;
    cin>>t;
    while(t>0)
        {
            long int a,x,y,p,i;
            cin>>a;
            if(a%2==0)
                {
                    x=1;
                    y=4;
                    for(i=2;i<a;i=i+2)
                        {
                            x=x+y;
                            y=y*4;
                        }
                }
            else
                {
                    x=1;
                    y=2;
                    for(i=1;i<a;i=i+2)
                        {
                            x=x+y;
                            y=y*4;
                        }
                }
            p=__gcd(y,x);
            x=x/p;
            y=y/p;
            cout<<x<<" "<<y<<" ";
            t--;
            }
return 0;
}

