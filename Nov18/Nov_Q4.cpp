#include <iostream>
#include<math.h>
#include <cstdlib>
#include <algorithm>
using namespace std;
bool comp(int x, int y)                                 //used for max_element function
{
    return (x < y);
}
int main()
{
    int n,st,k;
    cin>>n>>st>>k;
    int a[n],l[n]={0},b[n],p=0,i,j,q=5,temp;
    string s;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    cin>>s;
    for(j=0;j<q;j++)
    {
        if(s[j]=='?')                                                   //for '?'
{
    for(i=0;i<n;i++)
    {
        b[i]=a[i];
    }
    for(i=0;i<n;i++)                        //for finding max of subconsecuence of a i.e finding for '?'
    {
        if(b[i]==b[i+1]==1)
        {
            p++;
        }
        else
        {
            l[i]=p+1;
            i++;
            p=0;
        }
    }
 /*   for(i=0;i<n;i++)                            //for adding terms obtained in l[] due to more no. of 1's consecutively
    {
        if((l[i]!=0) && (l[i+1]!=0))
        {
            l[i+1]=l[i]+l[i+1];
            l[i]=0;
        }
    }*/
/*    for(i=0;i<n;i++)
    {
        cout<<l[i]<<"   ";
    }*/
    int *m;
m=max_element(l+0,l+n,comp);                                          //*m is the maximum element
if(*m<=k)
    cout<<*m<<endl;   //*m is the max value                                   //this will serve as the output of '?'
else
    {
        cout<<*m-1<<endl;                    //max value
    }
}
    else if(s[j]=='!')                                             //for '!'
    {
        for(i=0;i<n;i++)
        {
            b[0]=a[n];
            b[i+1]=a[i];
        }
    }
    }
	return 0;
}
