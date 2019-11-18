#include <iostream>
#include <map>

using namespace std;

bool is_prime(unsigned long int testing){
	if(testing <= 1 || testing == 4) return false;

	unsigned long int divisor = 2;
	unsigned long int max = testing / divisor; // rounds down if result is a decimal

	while(divisor < max){
		max = testing / divisor;
		if( (testing % divisor) == 0 )
			return false;
		++divisor;
	}

	return true;
}

int calcdigits(unsigned long int a){
	int numdigits = 0;
	while(a > 0){
		a /= 10;
		++numdigits;
	}
	return numdigits;
}


bool pandigital(unsigned long int num, const int digits){
	if(calcdigits(num) != digits) return false;

	bool onethroughnine[10] = {true,false,false,false,false,false,false,false,false,false};

	while(num > 0){
		if(num % 10 > digits || onethroughnine[num % 10]) return false;
		onethroughnine[num % 10] = true;
		num /= 10;
	}

	return true;
}

int main(){
	unsigned long int pannum = 0;
	int ndigit = 7;

// using math: 987654321 (or any combo) not prime, all divisible by 3 since all digits add up to number divisible by 3)
// using math: 87654321 (or any combo) not prime, all divisible by 3 since all digits add up to number divisible by 3)
// 7654321 doesn't follow this pattern, need to try all 7654321 combos from highest to lowest
// 654321 won't work, 54321 won't work, 321 won't work, 21 won't work, 1 not prime ... 4321 would need to be tried

/*	cout<<ndigit<<endl;
	for(pannum = 987654321; pannum > 123456788; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}
	--ndigit;
	cout<<ndigit<<endl;
	for(pannum = 87654321; pannum > 12345677; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}
	--ndigit;*/
	for(pannum = 7654321; pannum > 1234566; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}
/*	--ndigit;
	for(pannum = 654321; pannum > 123455; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}
	--ndigit;
	for(pannum = 54321; pannum > 12344; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}
	--ndigit;*/
	ndigit = 4;
	for(pannum = 4321; pannum > 1233; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}
/*	--ndigit;
	for(pannum = 321; pannum > 122; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}
	--ndigit;
	for(pannum = 21; pannum > 11; --pannum){
		if(pandigital(pannum, ndigit) && is_prime(pannum)){
			cout << "answer: " << pannum << endl;
			return 0;
		}
	}*/
}
