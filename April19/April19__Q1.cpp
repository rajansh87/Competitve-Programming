#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,i;
    cin>>n;
    long long int a[n];
    for(i=0;i<n;i++)
        cin>>a[i];

    sort(a,a+n);
    if((a[n-2]%a[n-1])>(a[n-1]%a[n-2]))
        cout<<(a[n-2]%a[n-1])<<endl;
    else
        cout<<(a[n-1]%a[n-2])<<endl;


    /*for(i=0;i<n;i++)
        cout<<a[i]<<"  ";*/
}
