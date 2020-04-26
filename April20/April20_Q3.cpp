#include<bits/stdc++.h>
using namespace std;
//int i,j;
int findTotalPrimeNumbers(int var)   //counts the prime numbers
{
    int number = 0;
    while(var%2==0)
        {
            number=number+1;
            var= var/2;
        }
    for(int i=3;i<sqrt(var);i=2+i)
     {
        if(var%i==0)
         {
            while(var%i==0)
             {
                var/=i;
                number++;
            }
        }
    }
    if(var>2)
     {
        number++;
     }
    return number;
}
bool checkPrime(int n)          //check a number is prime or not
{
    if(n<=1){return false;}
    if(n<=3){return true;}
    if(n%2==0 || n%3==0){return false;}
    for(int i=5;i*i<=n;i=i+6){if(n%i==0 || n%(i+2)==0){return false;}}
    return true;
}
void solve()                   //my workspace
{
    int num2;
    int num1;
    cin>>num1>>num2;
    if(num2!=1)
        {
            if(num1<pow(2,num2))
            {
                cout<<0<<endl;

            }
            else
            {
                cout<<(findTotalPrimeNumbers(num1)<num2?0:1)<<endl;
            }
        }
    else
        cout<<1<<endl;

}


int main()            //main function
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while(t>0)
    {
        solve();
        t--;
    }

    /*ll testcase=1;
    test
    {
        cout<<"Case #"<<testcase<<": ";
        solve();
        cout<<endl;

        testcase++;
    }*/
    return 0;
}
