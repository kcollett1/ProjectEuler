#include <iostream>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

bool is_palindrome_10(unsigned int num){
	vector <unsigned int> digits_holder;
	unsigned int digits = 0;

// parse digits out into vector
	while(num > 0){
		digits_holder.push_back(num % 10);
		num /= 10;
		++digits;
	}

// go through digits to check if palindrome or not
	for(int start = 0; start < digits/2; ++start)
		if(digits_holder[start] != digits_holder[digits - 1 - start])
			return false;

// either it made it through loop without failing or is only one digit
	return true;
}

bool is_palindrome_2(int num){
	//if(num <= 0) return false;

// write in binary and parse digits out into vector
	map <unsigned int, bool> digits_holder;
	int highestpower = 0;
	while(pow(2,highestpower) <= num) ++highestpower;
	--highestpower;
	const int digits = highestpower + 1;

	while(num > 0){
		if(num/pow(2,highestpower) >= 1){
			digits_holder[highestpower] = true;
			num -= pow(2,highestpower);
		}else digits_holder[highestpower] = false;
		--highestpower;
	}

// go through digits to check if palindrome or not
	for(int start = 0; start < digits/2; ++start)
		if(digits_holder[start] != digits_holder[digits - 1 - start])
			return false;

// either it made it through loop without failing or is only one digit
	return true;
}

int main(){
	int running_sum = 0;

	for(unsigned int i = 1; i < 1000000; ++i)
		if(is_palindrome_10(i) && is_palindrome_2(i))
			running_sum += i;

	cout << "answer = " << running_sum << endl;

}
