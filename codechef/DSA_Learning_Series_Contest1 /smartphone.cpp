#include <cstdio>
#include <algorithm>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
using namespace std;
int main()
{

    long long int t,m=0,i;
    cin>>t;
    long long int x[t];
    for(i=0;i<t;i++)
    {
        cin>>x[i];
    }
    sort(x, x+t);
    for (int i = 0; i < t; i++)
    {
        cout<<x[i]<<" ";
    }
    
    for(i=0;i<t;i++)
    {
        x[i]*=t-i;
        cout<<x[i];
         if(m<x[i])
        {
            m=x[i];
        }
    }
    
    cout<<m;
}