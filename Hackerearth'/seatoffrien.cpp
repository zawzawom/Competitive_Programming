#include <iostream>

#include <string.h>

using namespace std;

int main()

{

    int t;

    cin >> t;

    while (t--)

    {
        cout << "\n";

        int n;

        cin >> n;

        int q, r;

        q = n / 6;

        r = n % 6;

        char s[2];

        if ((r == 1) || (r == 0))

            strcpy(s, "WS");

        else if ((r == 2) && (r == 5))

            strcpy(s, "MS");

        else

            strcpy(s, "AS");

        if (q % 2 == 0)

        {

            cout << (6 * (q + 2) - r + 1) << " " << s;
        }

        else

        {

            cout << (6 * q - r + 1) << " " << s;
        }
    }
    return 0;
}