#include<iostream>
using namespace std;
int main()
{   int array[8] ={1,23,33,4,23,1000,73,3};
    int temp,i;
    bool test = true;
    while (test)
    { 
        test = false;
        for(i=0;i<8-1;i++)
        {
            if(array[i]<array[i+1])
            {
                temp = array[i];
                array[i]=array[i+1];
                array[i+1]=temp;
                test = true;

            }
        }
    }
    for ( i = 0; i < 8; i++)
    {
        cout<<array[i]<<" ";
    }
    
    
}