#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
int lcm(int,int);
//int gcd(int,int);

int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
       int a,b;
       cin>>a>>b;
      long long int p,q;
       q=__gcd(a,b);
       p=lcm(a,b);
       cout<<q<<" "<<p<<endl;


        t--;
    }
    return 0;
}
int lcm(int num1,int num2)
{
   int maxValue;
   maxValue = (num1 > num2) ? num1 : num2;
   while(1)
   {
      if((maxValue % num1 == 0) && (maxValue % num2 == 0))
      {
         //cout << "LCM: " << maxValue << endl;
         break;
      }
      ++maxValue;
   }
   return maxValue;
}
/*
int gcd(int x,int y)
{
   int i,gcd;
   for (i = 1; i <= x && i <= y; i++)
   {
      if (x % i == 0 && y % i == 0)
         gcd = i;
   }
   //cout << "\nGCD of " << x << " and " << y << " is: " << gcd << endl;
   return gcd;
}
*/
