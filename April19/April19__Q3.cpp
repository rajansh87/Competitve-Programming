#include<bits/stdc++.h>
using namespace std;
struct my
{
	int x;
	int y;
};
bool fun1(my l,my r) { return l.x < r.x; }
bool fun2(my l,my r) { return l.y < r.y; }
int main()
{
	long long int t;
	cin >> t;
	while(t--)
	{
        my a[100000];
	    long long int n,m,k,v=0,s=0,j;
	    cin>>n>>m>>k;

	    for(j=0;j<k;j++)
	    {
            cin>>a[j].x>>a[j].y;
		}

		//stable_sort(a, a + k,fun1);
		//stable_sort(a, a + k,fun2);

		for(j=0;j<k-1;j++)
	    {
	        if(a[j+1].x==a[j].x+1&&a[j+1].y==a[j].y)
	        	s++;
		}
		//stable_sort(a, a + k,fun2);
		//stable_sort(a, a + k,fun1);
		for(j=0;j<k-1;j++)
	    {
	         if(a[j+1].y==a[j].y+1&&a[j+1].x==a[j].x)
	        	s++;
		}
		s=4*k-2*s;
	cout<<s<<endl;
	}
	return 0;
}
