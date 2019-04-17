#include<iostream>
#include<string>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    cin.ignore();
    while(t>0)
    {
        int i=0;
        string s;
        string s2="not";
        getline(cin,s);
        int l=0;
        s=s+' ';
        l=s.length();
        string s1="";
        int z=0;
        for(i=0;i<l;i++)
        {
            if(s[i]!=' ')
                {
                    s1=s1+s[i];
                }
            else
            {
                int p=s1.compare(s2);
                if(p==0)
                {
                    z=1;
                    s1="";
                    break;
                }
                else{s1="";}
            }
        }
        if(z==1)
        {
            cout<<"Real Fancy\n";
        }
        else
        {
            cout<<"regularly fancy\n";
        }

        t--;
    }
return 0;
}
