#include <bits/stdc++.h>
using namespace std;
typedef long long int lld;

lld count(lld a, lld b, lld c, lld mid)
{
    return ((mid/a)+(mid/b)+(mid/c)-(mid/((a*b)/__gcd(a, b))) - (mid/((b*c)/__gcd(b, c))) - (mid/((a*c)/__gcd(a, c))) + ((mid / ((((a*b)/__gcd(a, b))* c) / __gcd(((a*b)/__gcd(a, b)), c)))));
}

int main() 
{
	lld n, a, b, c;
	cin>>n>>a>>b>>c;
	
	lld left=1, right=INT_MAX, mid;
	
	while(left<right)
	{
	    mid=left+(right-left)/2;
	    
	    if(count(a, b, c, mid)<n)
	        left=mid+1;
	    else right=mid;
	}
	
	cout<<left;
	return 0;
}
