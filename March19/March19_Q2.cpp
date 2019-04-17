#include<bits/stdc++.h>
using namespace std;
long long int findValue(long long int arr[],long long int s)
{
    long long int i,num=0,r=0;
    for(i=0;i<s;i++)
    {
        num=arr[i];
        r=r*10+num;
    }
    return r;
}
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n,d;
        cin>>n>>d;
        long long int i,dig=0;
        i=n;
        while(i>0)
        {
            i=i/10;
            dig++;
        }
        long long int x,p=n,a[dig],q,k,min=10000000000,temp,l,j,k2=0;
        for(i=0;i<dig;i++)
        {
            x=p%10;
            p=p/10;
            a[dig-i-1]=x;
        }
        for(i=0;i<dig;i++)
        {
            if(a[dig-1-i]>=d)
                {
                    p=findValue(a,dig);
                    a[dig-1-i]=d;
                    q=findValue(a,dig);
                    if(p<q)
                    {
                        break;
                    }
                    else
                    {
                        for(j=dig-1-i;j<dig-1;j++)
                        {
                            temp=a[j];
                            a[j]=a[j+1];
                            a[j+1]=temp;
                            //k=findValue(a,dig);
                        }

                        //cout<<"min : "<<min<<endl;
/*
                       for(l=0;l<dig;l++)
                        {
                            x=min%10;
                            min=min/10;
                            a[dig-l-1]=x;
                        }
  */                  }
                }
        }
       /*p=findValue(a,dig);
        cout<<p<<endl;*/
        ////////////////////////////////////////////////////////

        for(k2=0;k2<dig;k2++)
        {for(i=0;i<dig-1;i++)
        {
            while(a[i]>a[i+1])
            {
                for(j=i;j<dig;j++)
                    {
                        a[j]=a[j+1];
                    }
                    a[dig-1]=d;
            }
        }
        }
        p=findValue(a,dig);
        cout<<p<<endl;

    }

return 0;
}
