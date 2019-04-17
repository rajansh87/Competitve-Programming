#include<iostream>
#include<string>
#include<stdlib.h>
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
        getline(cin,s);

        i=s.find("not");

        if(((s[i-1]==' ')&&(s[i+3]==' '))||((s[i-1]==' ')&&(s[i+3]=='\0'))||((i==0)&&(s[i+3]==' '))||((s[i-1]==' ')&&(s[i+3]=='\n')))
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
