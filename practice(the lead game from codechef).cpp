#include <iostream>
#include <cstdlib>
#include<math.h>
#include <algorithm>
using namespace std;
bool comp(int x, int y)                                 //used for max_element function
{
    return (x < y);
}
int main()
{
int n;
cin>>n;
int a[n],s1=0,b[n],s2=0,c[n],pos,q=0;
int i;
for(i=0;i<n;i++)
{
    cin>>a[i]>>b[i];
    s1=s1+a[i];
    s2=s2+b[i];
    c[i]=abs(s1-s2);

}
/*for(i=0;i<n;i++)
{
    cout<<c[i]<<endl;
}*/
int *m;
m=max_element(c+0,c+n,comp);                                          //*m is the maximum element
//cout<<"max is : "<<*m<<endl;
for(i=0;i<n;i++)                                                                  //for searching *m in c[i]
{
    if(c[i]==*m)
    {
        q=1;
        pos=i+1;
        break;
    }
}
//cout<<"\n Element Found At Position "<<pos<<endl;
if(a[pos-1]>b[pos-1])
    cout<<"1 "<<*m<<endl;
else
    cout<<"2 "<<*m<<endl;
return 0;
}
