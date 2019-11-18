#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool is_prime(int testing){
	if(testing <= 1 || testing == 4) return false;

	int divisor = 2;
	int max = testing / divisor; // rounds down if result is a decimal

	while(divisor < max){
		max = testing / divisor;
		if( (testing % divisor) == 0 )
			return false;
		++divisor;
	}

	return true;
}

bool r_to_l(int checknum){
	while(checknum > 0){
		if(!is_prime(checknum)) return false;
		checknum /= 10;
	}

	return true;
}

bool l_to_r(int checknum){
	int digits = 1, tmp = checknum;
	while((tmp /= 10) > 0) ++digits;

	while(digits > 0){
		if(!is_prime(checknum)) return false;
		checknum -= int(checknum / pow(10,digits - 1)) * pow(10,digits - 1);
		--digits;
	}
	return true;
}

int main(){
	int numtrunctables = 0;
	int sumtrunctables = 0;

	for(int i = 22; numtrunctables < 11; ++i){
		if(r_to_l(i) && l_to_r(i)){
			++numtrunctables;
			sumtrunctables += i;
		}
	}

	cout << "answer: " << sumtrunctables << endl;
}
