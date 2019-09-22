#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
long long fast_power(long long base, long long power) {
    long long result = 1;
    while(power > 0) {

        if(power % 2 == 1) { // Can also use (power & 1) to make code even faster
            result = (result*base) % MOD;
        }
        base = (base * base) % MOD;
        power = power / 2; // Can also use power >>= 1; to make code even faster
    }
    return result;
}
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int k,p=fast_power(10,9)+7,i,x=10;
        cin>>k;
        i=1;
        /*while(i<k)
        {
            x=x*2;

            i=i+1;
        }*/
        if(k!=1)
            x=x*fast_power(2,k-1);


        cout<<x%p<<endl;

    }


    return 0;
}
