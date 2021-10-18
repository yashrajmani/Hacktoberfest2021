
// A number is called happy if it leads to 1 after a sequence of steps wherein each step number is 
// replaced by the sum of squares of its digit that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1. 

#include <bits/stdc++.h>
using namespace std;


int numSquareSum(int n)
{
	int squareSum = 0;
	while (n)
	{
		squareSum += (n % 10) * (n % 10);
		n /= 10;
	}
	return squareSum;
}

// returns true if n is Happy number
bool isHappynumber(int n)
{  //floyd's algorithm is used here
	int slow, fast;

	// initialize slow and fast by n
	slow = fast = n;
	do
	{
		// move slow number by one iteration
		slow = numSquareSum(slow);

		// move fast number by two iteration
		fast = numSquareSum(numSquareSum(fast));

	}
	while (slow != fast);

	// if both number meet at 1, then return true and if it enters a cycle then false
	return (slow == 1);
}


int main()
{
	int n;
  cin>>n;
	if (isHappynumber(n))
		cout << n << " is a Happy number\n";
	else
		cout << n << " is not a Happy number\n";
}
