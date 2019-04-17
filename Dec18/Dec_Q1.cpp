#include <iostream>
#include<cstdlib>
#include<ctime>
using namespace std;


//   int rand();
int main() {

	int x,y,z;
	srand(time(NULL));
	x=(rand()%3)+1;
	if(x!=0)
	{
	    cout<<x<<endl;
	}
	else
	{
	    x++;
	    cout<<x<<endl;
	}
	cin>>y;
	srand(time(NULL));
	z=(rand()%3)+1;
	if(z!=0)
	{
	    cout<<z<<endl;
	}
	else
	{
	    z++;
	    cout<<z<<endl;
	}
	return 0;
}
