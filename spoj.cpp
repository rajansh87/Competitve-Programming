#include <iostream>
#include <string>
using namespace std;

int main() {

    string s1,s2;
    cin>>s1>>s2;
    int l1,l2;
    l1=s1.length();
    l2=s2.length();
    cout<<l1<<" "<<l2<<endl;
    cout<<(s1+s2)<<endl;
    char temp;
    temp=s1[0];
    s1[0]=s2[0];
    s2[0]=temp;
    cout<<s1<<" "<<s2<<endl;

    return 0;
}

