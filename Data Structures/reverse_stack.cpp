#include<bits/stdc++.h>
using namespace std;
int top=-1;
void push(int stack[], int size,int n)
{
 //   if(top==size-1)
      //  cout<<"\n\tStack is Full ";
   // else
    //{
       top++;
        stack[top]=n;
    //}
}
void pop(int stack[],int size)
{
    if(top==-1)
        cout<<"\n\tStack is Empty ";
    else
    {
        cout<<"\nThe "<<stack[top]<<" Element Deleted Successfully ";
        top--;
    }
}
int size()
{
    return top+1;
}

int main()
{
    int a[6];
    int n=6;
    int i;
    for(i=0;i<n;i++)
        cin>>a[i];

    int b[6];
    for(i=0;i<n;i++)
    {
        push(b,6,a[i]);
    }
    for(i=0;i<n;i++)
        cout<<b[i]<<" ";

return 0;
}
