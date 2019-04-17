#include <iostream>
using namespace std;

int main() {
	int t,n;
	cin>>t;
	while(t>0)
	{
	    cin>>n;
	    int a[n];
	    int i,x,y,j;
	    for(i=1;i<=n;i++)
        {
            cin>>a[i];
        }
        int p=0,q=0;
        for(i=1;i<=n;i++)
        {
            x=a[i];
            for(j=i+1;j<=n;j++)
            {
                y=a[j];
                if((x!=y)&&(a[x]==a[y]))
                {
                    p++;
                }
                else
                {
                    q++;
                }
            }
        }
        if(p>0)
        {
            cout<<"Truly Happy\n";
        }
        else
            cout<<"Poor Chef\n";
	    t--;
	}
	return 0;
}
