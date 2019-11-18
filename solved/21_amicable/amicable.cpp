#include <iostream>

using namespace std;

int add_divisors(const int num){
	if(num == 1){ return 0; }
	if(num == 4){ return 3; }

	int sum = 1;
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

// find sum of all amicable numbers under 10000
int main(){
	int running_sum = 0;

	int divis[10000];
	for(int i = 1; i < 10000; ++i) divis[i] = add_divisors(i);

	int amic[10000]; // so we don't repeat pairs
	for(int i = 1; i < 10000; ++i) amic[i] = 0;

	for(int i = 1; i < 10000; ++i){
		if(amic[i] != 0) continue;

		// divis[i] = n --> so check if divis[ divis[i] ] == i
		if(divis[i] < 10000){
			if(divis[i] != i && divis[divis[i]] == i){
				amic[divis[i]] = 1;
				running_sum += (i + divis[i]);
			}
		}else{ if(add_divisors(divis[i]) == i){ running_sum += i; } }
	}

	cout << "sum of all amicable numbers less than 10000 is " << running_sum << endl;
}
