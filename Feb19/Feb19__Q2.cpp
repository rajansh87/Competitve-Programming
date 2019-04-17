#include<bits/stdc++.h>
#include<string>
using namespace std;

#define SIZE 26
void printCharWithFreq(string str,int main_n)
{
    int n = str.size();
    int count=0;
    int freq[SIZE];
    memset(freq, 0, sizeof(freq));
    for (int i = 0; i < n; i++)
        freq[str[i] - 'a']++;

    for (int i = 0; i < n; i++) {
        if (freq[str[i] - 'a'] != 0) {
          //  cout << str[i] << freq[str[i] - 'a'] << " ";
            if(freq[str[i] - 'a']==main_n)
                count++;
            freq[str[i] - 'a'] = 0;
        }
    }
    cout<<count<<endl;
}

string removeDuplicatesFromString(string str)
{
    int counter = 0;

    int i = 0;
    int size = str.size();

    int x;
    int length = 0;

    while (i < size) {
        x = str[i] - 97;
    if ((counter & (1 << x)) == 0) {
            str[length] = 'a' + x;
            counter = counter | (1 << x);
            length++;
        }
        i++;
    }

    return str.substr(0, length);
}
int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        int n,i;
        cin>>n;
        string main;
        string s1;
        i=0;
        while(i<n)
        {
            cin>>s1;
            main=main+removeDuplicatesFromString(s1);
            i++;
        }

//cout<<main<<endl;

sort(main.begin(), main.end());
//cout<<main<<endl;
printCharWithFreq(main,n);

        t--;
    }
return 0;
}
