#include<bits/stdc++.h>
using namespace std;
int substring(string s, char c,long long int num)
{
    long long int i,j,count=0;
    string frag;
        i=0;
        j=1;
        while(j<=num-i && i<num)
        {
            frag=s.substr(i,j);
           // cout<<"string : "<<frag<<endl;
            if(frag.find(c)>=0 && frag.find(c)<num)
                count++;
            j++;
            if(j==num-i+1)
            {
                //cout<<"iter : "<<endl;
                i++;
                j=1;
            }

        }
    return count;
}
int count(string s, char c)
{
    int res = 0;

    for (int i=0;i<s.length();i++)
        if (s[i] == c)
            res++;

    return res;
}
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
    long long int n;
    string str;
    char ch;
    cin>>n;
    cin>>str;
    cin>>ch;
    long long p=count(str,ch);
    long long int co=0;
    if(p==n)
    {
        co=n;
    }
    else
    {
    co=substring(str,ch,n);
    }
    cout<<co<<endl;

   }
    return 0;
}

