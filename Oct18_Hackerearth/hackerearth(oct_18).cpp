#include<iostream>
using namespace std;
int main()
{
int n,a,b,c=0,i,t;
cin>>t;
while(t>0)
{c=0;
    cin>>n>>a>>b;
for(i=-n;i<=n;i++)
{
    c++;
}
cout<<c<<endl;
t--;
}return 0;
}
