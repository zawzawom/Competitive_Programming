#include<iostream>
using namespace std;
int main()
{
    int testCase;
    cin>>testCase;
    while(testCase--)
    {
        int number,reverse=0,num=0;
        cin>>number;
        while (number!=0)
        {
           reverse = (number%10);
           num = num*10+reverse;
           number = number/10;
       }
        cout<<num<<endl;
    }
}