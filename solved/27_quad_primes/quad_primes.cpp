#include <iostream>

using namespace std;

bool is_prime(int testing){
	if(testing <= 1 || testing == 4) return false;

	int divisor = 2;
	int max = testing / divisor; // rounds down if result is a decimal
	bool isprime = true;

	while(divisor < max){
		max = testing / divisor;
		if( (testing % divisor) == 0 ){
			isprime = false;
			break;
		}
		++divisor;
	}

	return isprime;
}

int main(){
	int max = 0;
	int maxprod = 0;
	for(int a = -999; a < 1000; ++a){
		for(int b = -1000; b < 1001; ++b){
			int n = 0;
			while(is_prime(n*n+a*n+b)) ++n;
			if(n == 71) cout << "n=71" << endl;
			if( max < n ){
				maxprod = a*b;
				max = n;
			}
		}
	}
	cout << "maximum product of coefficients producing most "
	     << "consecutive prime numbers is " << maxprod << endl;

	return 0;
}
