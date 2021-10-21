// Nearest and previous smaller element

#include <bits/stdc++.h>

using namespace std;

void nearestElement(int a[], int n)
{
     stack<int> st;
     for (int i = 0; i < n; i++)
     {
          while (!st.empty() && st.top() >= a[i])
          {
               st.pop();
          }
          if (st.empty())
          {
               cout << "-1 ";
          }
          else
          {
               cout << st.top() << " ";
          }

          st.push(a[i]);
     }
}

int main()
{
     int a[] = {4, 10, 5, 18, 3, 12, 7};
     int n = sizeof(a) / sizeof(a[0]);
     nearestElement(a, n);
     return 0;
}
