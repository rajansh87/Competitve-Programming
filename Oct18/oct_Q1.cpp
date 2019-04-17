#include<iostream>
using namespace std;
int main()
{
int s=0,T,P1,P2,K;
cin>>T;
while(T>0)
{
cin>>P1>>P2>>K;

s=P1+P2;
s=s/K;
if(s%2==0)
{
    cout<<"CHEF"<<endl;
}
else
    cout<<"COOK"<<endl;
T--;
}
return 0;
}
