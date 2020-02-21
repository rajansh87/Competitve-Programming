#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define loop1 for(i=0;i<n;i++)
#define loop2 for(j=0;j<n;j++)
#define loopi(a,b) for(i=a;i<b;i++)
#define loopj(a,b) for(j=a;j<b;j++)
#define rloopi(a,b) for(i=a;i>b;i--)
#define rloopj(a,b) for(j=a;j>b;j--)
#define test long long int t;cin>>t;while(t--)
#define loopvar(var,a,b) for(var=a;var<b;var++)
#define rloopvar(var,a,b) for(var=a;var>b;var--)
set<ll> x;
ll myArray3[4];
ll value;
void func(ll** myArray,ll i)
{
	if(i==4)      // it is recursive function
        {
            ll myArray2[4]; //array
            loopi(0,4)
            {
                myArray2[i]=myArray3[i];
            }
            sort(myArray2,myArray2+4);  //sort array
            ll money=0;
            if(myArray2[0]==0)
                {
                    money=money-100;       //penalty
                }
            else
                {
                    money=money+myArray2[0]*25;
                }
            if(myArray2[1]==0)
                {
                    money=money-100;         //penalty
                }
            else
                {
                    money=money+myArray2[1]*50;
                }
            if(myArray2[2]==0)
                {
                    money=money-100;            //penalty
                }
            else
                {
                    money=money+myArray2[2]*75;
                }
            if(myArray2[3]==0)
                {
                    money=money-100;               //penalty
                }
            else
                {
                    money=money+myArray2[3]*100;
                }
            if(money>::value)
                {
                    ::value=money;              //final
                }
            return;
        }
        ll j;
        loopj(0,4)
        {
            if(x.find(j)==x.end())
                {
                    x.insert(j);                  //inert in set
                    myArray3[i]=myArray[i][j];
                    func(myArray,i+1);             // again callthe dame function i.e recursion
                    myArray3[i]=-1;
                    x.erase(j);
                }
        }
        return;
    }
int main()
{
    ll total = 0;
    test                    //testcase
    {
        ll n,i,j;
		cin>>n;

		::value=INT_MIN;               //min value

		ll**myArray=new ll*[4];

		for(i=0;i<4;i++)                 //create 2D array initialised to 0
            {
                myArray[i]=new ll[4];
                for(j=0;j<4;j++)
                {
                    myArray[i][j]=0;
                }
            }
        while(n>0)              //requests
        {
			ll x;                 //timming
			char ch;                //movie
			cin>>ch>>x;

			if(ch=='B')
			{
				myArray[1][(x/3)%4]++;
			}
			else if(ch=='A')
			{
				myArray[0][(x/3)%4]++;
			}
			else if(ch=='C')
			{
				myArray[2][(x/3)%4]++;
			}
			else
			{
				myArray[3][(x/3)%4]++;
			}
			n--;
		}
		func(myArray,0);                        //function call

		total+=::value;

		cout<<::value<<endl;                    //testcase answer
    }
    cout<<total;                                //total testcases answer
    return 0;
}
