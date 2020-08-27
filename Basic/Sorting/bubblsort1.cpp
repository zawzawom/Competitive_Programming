#include<iostream>
using namespace std;
int main()
{ int n=8;
  int array[8] ={1,23,33,4,23,1000,73,3};
  int temp,i,j;
  for(i=0;i<n-1;i++)
  {
   for(j=0;j<n-i-1;j++)
   {
       if(array[j]<array[j+1])
       {
           temp       = array[j];
           array[j]   = array[j+1];
           array[j+1] = temp;
       }
   }
  }
  for ( i = 0; i < n; i++)
  {
      cout<<array[i]<<" ";
  }
  

}