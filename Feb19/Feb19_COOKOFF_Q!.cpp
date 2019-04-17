 #include<bits/stdc++.h>
 using namespace std;
 int main()
 {
int t;
cin>>t;
while(t>0)
{
    int n,b;
    cin>>n>>b;
    int w[n],h[n],p[n],i;
    for(i=0;i<n;i++)
    {
        cin>>w[i]>>h[i]>>p[i];
    }
    int max=0,area=0,count=0;
    for(i=0;i<n;i++)
    {
        if(p[i]<=b)
        {
            area=w[i]*h[i];
            if(max<area)
            {
                max=area;
            }
            count++;
        }
    }
if(count>0)
    {
        cout<<max<<endl;
    }
else
{
    cout<<"no tablet\n";
}

    t--;
}

 return 0;
 }
