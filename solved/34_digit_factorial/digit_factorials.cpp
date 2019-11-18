#include <iostream>

using namespace std;

int main(){
	int factorials[10] = {1,1,2,6,24,120,720,5040,40320,362880};
	const int max = 1000000000;
	int running_sum = 0;

	for(int itr = 11; itr <= max; ++itr){
		int tmp = itr;
		int sum = 0;
		while(tmp > 0 && sum <= itr){
			sum += factorials[tmp%10];
			tmp /= 10;
		}
		if(itr == sum){
			running_sum += sum;
			cout << sum << " ... " << running_sum << endl;
		}
	}
}
