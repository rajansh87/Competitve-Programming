#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T>0)
    {
        long long int n;
        cin >> n;
       long long a[n],d[n];
       vector <long long> v;
       long long int i;
       for(i=0;i<n;i++)
       {
           cin>>a[i];
       }
       for(i=0;i<n;i++)
       {
           cin>>d[i];
       }
for(i=0;i<n;i++)
       {
            if(i==n-1)
            {
                if(d[i]>a[i-1]+a[0])
                {
                    v.push_back(d[i]);
                }
            }
            else if(i==0)
            {
                if(d[i]>a[i+1]+a[n-1])
                {
                    v.push_back(d[i]);
                }
            }
            else
            {
                if(i>0 && i<n-1)
                {
                    if(d[i]>a[i-1]+a[i+1])
                    {
                        v.push_back(d[i]);
                    }
                }
            }
       }
       if(!v.empty())
       {
           //sort in vector v
           sort(v.begin(),v.end());
           //size of v in l
           long long l=v.size()-1;

           cout<<v[l]<<endl;
       }
       else
       {
           cout<<"-1\n";
       }

T--;
    }
    return 0;
}
