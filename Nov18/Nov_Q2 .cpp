#include <iostream>
#include<math.h>
using namespace std;

int main()
{
	int x=1,i,t;
	cin>>t;
	int a1[50],y[100];
    for(i=1;i<=t;i++)
        {
            cin>>a1[i];
            y[2*i]=pow(2,a1[i]);
        }
    for(i=1;i<=t;i+2)
	    {
	        y[i]=1;
	    }
    for(i=1;i<=t;i++)
    {
        cout<<y[i]<<"  ";
    }
	return 0;
}
