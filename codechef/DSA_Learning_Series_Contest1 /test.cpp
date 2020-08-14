#include<iostream>
using namespace std;
int main()
{
   int num;
   int i =0;
   do 
   {
       cin>>num;
       
       if (num==42)
       {
           return 0;
       }
       cout<<num<<"\n";
   }while (num!=42);
    return 0;
}