#include <iostream>

using namespace std;

unsigned long int add_divisors(const int num){
	if(num == 1){ return 0; }
	if(num == 4){ return 3; }

	unsigned long int sum = 1;
	int divisor = 2;
	int max = num / divisor; // rounds down if result is a decimal

	while(divisor < max){
		max = num/divisor;
		if((num%divisor) == 0){
			if(divisor == max) sum += divisor;
			else sum += (divisor + max);
		}
		++divisor;
	}

	return sum;
}

int main(){
// 1 - 28123 (12 is smallest abundant_num, 24 is smallest nonabundant_sum)
	unsigned long int sum_nonabundant_sums = 276; // sum of 1 to 23
	bool abundant_nums[28112];
	bool abundant_sums[28124];

	for(int i = 24; i < 28124; ++i) abundant_sums[i] = false;
	for(int i = 12; i < 28112; ++i)
		if(add_divisors(i) > i) abundant_nums[i] = true;
		else abundant_nums[i] = false;

	for(int i = 12; i < 28112; ++i){
		int j = i;
		for(; j < 28112; ++j){
			if(i+j > 28123) break;
			if(abundant_sums[i+j]) continue;
			if(abundant_nums[i] && abundant_nums[j])
				abundant_sums[i+j] = true;
			else abundant_sums[i+j] = false;
		}
	}

	for(int i = 24; i < 28124; ++i)
		if(!abundant_sums[i]) sum_nonabundant_sums += i;

	cout << "the sum of positive integers that can't be written as "
	     << "the sum of two abundant numbers is: " << sum_nonabundant_sums
	     << endl;
}
