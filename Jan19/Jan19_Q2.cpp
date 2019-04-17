#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        long long int n,a,b,c=0,d=0;
        cin>>n>>a>>b;
       long long int arr[n];
        long long int i,k=0;
       /* for(i=0;i<n;i++)
        {
            cin>>arr[i];
        }*/
        for(i=0;i<n;i++)
        {
            cin>>k;
            if(k%a==0)
            {
                //arr[i]=-1;               //random value = -1
                c++;
            }
            else if(k%b==0)
            {
                //arr[i]=-1;              //random value = -1
                d++;
            }
        }
        if(c>0)
        {
            if(d>0)
            {
                cout<<"ALICE\n";
            }
            else
            {
                cout<<"BOB\n";
            }
        }
        else
        {
            cout<<"ALICE\n";
        }
       // cout<<"\n\n\t\tc= "<<c<<"      d= "<<d<<endl;

        t--;
    }
return 0;
}
