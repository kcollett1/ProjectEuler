#include <iostream>
#include <vector>
#include <map>
#include <cmath>

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

bool circular_prime(int num, int& digits, vector<int>& store_circnums){
	vector <int> digits_holder;
	int tmp = num;

	while(tmp > 0){
		digits_holder.push_back(tmp % 10);
		tmp /= 10;
		++digits;
	}

	for(int start = 2; start <= digits; ++start){
		int circ_num = 0;

		for(int number = digits; number >= 1; --number){
			if(digits_holder[(number + digits - start) % digits] == 0)
				continue;

			circ_num += digits_holder[(number + digits - start) % digits] *
				    pow(10, number - 1);
		}
		if(!is_prime(circ_num)) return false;
		else store_circnums.push_back(circ_num);
	}

	store_circnums.push_back(num);

	return true;
}

int main(){
	map<int,bool> circularcheck;
	int circular_primes = 0;


	for(int i = 2; i < 1000000; ++i){
		if(circularcheck.count(i) > 0) continue;
		if(!is_prime(i)) continue;
// i is prime and we haven't checked it yet

		int digits = 0;
		vector<int> store_circnums;

		if(circular_prime(i, digits, store_circnums)){
			for(int i = 0; i < store_circnums.size(); ++i){
				if(circularcheck.count(store_circnums[i]) > 0) continue;
				circularcheck[store_circnums[i]] = true;
				++circular_primes;
			} // in case there are any repeat numbers, i.e. 11, 353
		}
	}


	cout << "answer = " << circular_primes << endl;
}
