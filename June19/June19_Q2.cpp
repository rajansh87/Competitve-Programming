#include<bits/stdc++.h>
#include<string>
using namespace std;
int main()
{
   // cout<<char(84);

    long long int t;
    cin>>t;
    while(t--)
    {
        string n;

        long long int x,dig=0,digsum=0,i,mul=1;
        cin>>n;
            dig=n.length();
            for(i=0;i<dig;i++)
            {
                x=int(n[i])-48;
                digsum=digsum+x;
            }
        i=1;
        while(digsum>mul)
        {
            mul=10*i;
            i++;
        }/*
        string s=string(mul-digsum+48);
        n.append(s);
*/

        cout<<n<<(mul-digsum)<<endl;
    }
    return 0;
}
