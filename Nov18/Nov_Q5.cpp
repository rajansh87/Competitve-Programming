#include <iostream>
#include<math.h>
using namespace std;
int checkprime(int);
int main()
{
int n;
cin>>n;
int v[n],i,j,p,q;
for(i=0;i<n;i++)
{
    cin>>v[i];
}
for(i=0;i<n;i++)
{
    for(j=i+1;j<n;j++)
    {
        p=v[i]+v[j];
        q=checkprime(p);
        if(q==1)
        {
            cout<<i+1<<" "<<j+1<<endl;
        }
    }
}


	return 0;
}
int checkprime(int x)
{
 int i, flag = 0,r;
    for(i=2; i<=x/2; ++i)
    {
        // condition for nonprime number
        if(x%i==0)
        {
            flag=1;
            break;
        }
    }

    if (flag==0)
        r=1;
    else
        r=0;
return r;
}

