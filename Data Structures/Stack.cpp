#include<bits/stdc++.h>
using namespace std;
int top=-1;
void push(int stack[], int size)
{
    int n;

    if(top==size-1)
        cout<<"\n\tStack is Full ";
    else
    {
        cout<<"\nEnter Number to Insert : ";
        cin>>n;
        top++;
        stack[top]=n;
    }
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
    int a[5],ch;
    while(1)
    {
        cout<<"\n1. Push \n2. Pop\n3. Traverse\n4. Exit";
        cout<<"\nEnter Your choice : ";
        cin>>ch;
        switch(ch)
        {   case 1: push(a,5);
                    break;
            case 2: pop(a,5);
                    break;
            case 3: int i;
                    cout<<" \n\n\n\t";
                    for(i=0;i<size();i++)
                        cout<<a[i]<<"  ";
                    cout<<"\n\n\n";
                    break;
            case 4: return 0;
        }
    }

return 0;
}
