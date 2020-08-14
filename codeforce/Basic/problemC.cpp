#include<iostream>
#include<algorithm>
using namespace std;
int main()
{   int TestCase;
    cin>>TestCase;
    for (int i = 0; i < TestCase; i++)
    {
        int numCar,timeTake;
        cin>>numCar>>timeTake;
        int arra[numCar];
        for (int j = 0; j < numCar; j++)
        {
            cin>>arra[j];
            sort(arra,arra+numCar);
       
        }
        for (int i = 0; i < numCar; i++)
        {
             if(arra[i+1]-arra[i]>timeTake)
             {
                cout<<"NO"<<"\n";
            }
        }
        cout<<"Yes\n";
        
        
    
    }
    

    return 0;
}
