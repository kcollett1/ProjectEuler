#include <iostream>
#include <cmath>

using namespace std;

int calcdigits(int a){
	int numdigits = 0;
	while(a > 0){
		a /= 10;
		++numdigits;
	}
	return numdigits;
}

bool pandigital(unsigned long int num){
	if(calcdigits(num) != 9) return false;

	bool onethroughnine[10] = {true,false,false,false,false,false,false,false,false,false};

	while(num > 0){
		if(onethroughnine[num % 10]) return false;
		onethroughnine[num % 10] = true;
		num /= 10;
	}

	return true;
}

int main(){
	unsigned long int long_pan = 0;
	unsigned long int pan_num = 0;
	for(unsigned int integer = 2; integer < 9877; ++integer){
		int ctr = 1;
		pan_num = integer;
		while(calcdigits(pan_num) < 9){
			++ctr;
			pan_num = (pan_num * pow(10,calcdigits(integer*ctr))) + integer*ctr;
		}

		if(pandigital(pan_num) && pan_num > long_pan) long_pan = pan_num;
	}

	cout << "answer: " << long_pan << endl;
}
