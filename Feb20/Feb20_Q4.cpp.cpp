#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
while(t>0)
{
    int n,price;
    cin>>n>>price;
    int a[n];
    int ansArray[n]={0};
    bool var=true;
    int x;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    x=a[0];
    for(int i=1;i<n;i++)
    {
        if(a[i]%x!=0)
        {
            var=false;
        }
        x=a[i];
    }
    if(price%a[n-1]==0)
    {
        if(var==true)
        {
            cout<<"NO"<<endl;
        }
    }
    else
    {
       cout<<"YES";
    for(int i=n-1;i>=0;i--)
    {
        int temp;
        if(price<=0)
        {
            //ansArray[i]=(p/a[i])+1;
            break;
        }
        else
        {
            if(price%a[i]!=0)
            {
                temp=price/a[i];
                ansArray[i]=temp+1;
                break;

            }
            else
            {
                temp=price/a[i];
                temp=temp-1;
                price=price-a[i]*temp;;
                ansArray[i]=temp;

            }
        }
    }

    for(int i=0;i<n;i++)
    {
        cout<<" ";
        cout<<ansArray[i];
    }
    cout<<endl;
    }
    t=t-1;
}

return 0;
}
