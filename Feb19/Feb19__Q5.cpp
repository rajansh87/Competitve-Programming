#include<bits/stdc++.h>
using namespace std;
/*int countReduce(string& str)
{
    int n = str.length();
    int res = 0;

    for (int i = 0; i < n / 2; i++)
        res += abs(str[i] - str[n - i - 1]);

    return res;
}*/


int cost(string str)
{
    int len = str.length();
    int res = 0;
    for (int i=0, j=len-1; i < j; i++, j--)
        if (str[i] != str[j])
            res += min(str[i], str[j]) - 'A' + 1;
    return res;
}
int countChar(char ch, string s)
{
    int i,count=0;
    for(i=0;i<s.length();i++)
    {
        if(s[i]==ch)
        {
            count++;
        }
    }
    return count;
}
int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        string a;
        int len=0,i,ans=0,count=0;
        cin>>a;
        string b=a;
        len=a.length();
        string s1=" ";

        a.insert(len/2,s1);

       string a1;
        string a2;
         for(i=0;a[i]!=' ';i++)
         {
             a1=a1+a[i];
         }
         while(a[i]!='\0')
         {
             a2=a2+a[i];
             i++;
         }
int max=0;
int count1=0,count2=0,count3=0;
if(len%2==0)
{
   count3=cost(b);
//count3=countReduce(a);
     /*for (i=0;i<len/2;i++)
       {
        if (a[i]!=a[len-i-1])
            count3++;
       }

cout<<"count = "<<count3<<endl;*/

         for(i=0;i<a1.length();i++)
         {
             count1=countChar(a1[i],a1);
             count2=countChar(a1[i],a2);
             if(count1!=count2)
             {
                 ans++;
             }
         }
         if(ans>count3)
            ans=count3;

}

     else if(len%2!=0)
        { max=0;
            for(i=0;i<len;i++)
            {
                count=countChar(a[i],a);
                if(count>len/2)
                {
                    ans=len-count;
                    break;
                }
                else
                {
                    if(max<count)
                    {
                        max=count;
                        ans=len-max;
                    }

                }
            }

        }
        cout<<ans<<endl;;
        t--;
    }
return 0;
}
