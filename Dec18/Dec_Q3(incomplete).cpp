#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
int n,c=0,p,cost=0,co=0;
cin>>n>>c;
int y;
y=(rand()%10)+1;

while(y<=n)
{
cout<<"1 "<<y<<endl;
cin>>p;

if(p==0)
{
    cout<<"2\n";

    co++;
}
if(p==1)
{
    cout<<"2\n";
    if(co>0)
    {
        cout<<"3 "<<y<<endl;
        break;
    }

}

//y++;
y=(rand()%10)+1;
}
return 0;
}

