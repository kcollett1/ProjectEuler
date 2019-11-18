#include <iostream>
#include <cmath>

using namespace std;

int main(){
	const int max = 10000000;
	int running_sum = 0, digit_sum = 0;

	for(int itr = 11; itr < max; ++itr){
		int i = itr;
		while(i > 0 && digit_sum <= itr){
			digit_sum += pow(i % 10, 5);
			i /= 10;
		}

		if(digit_sum == itr) running_sum += itr;

		digit_sum = 0;
	}

	cout << running_sum << endl;
}
