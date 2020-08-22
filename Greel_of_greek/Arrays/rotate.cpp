#include <iostream>
using namespace std;

int main() {
	int T;
    cin>>T;
	while(T--)
    {
        int N,D,i;
        cin>>N>>D;
        long long array[N];
        for (i = 0; i < N; i++)
        {
            cin>>array[i];
        }
        for ( i = 0; i < N; i++)
        {
            cout<<array[(i+D)%N]<<" ";
        }
        
        
    }
	return 0;
}