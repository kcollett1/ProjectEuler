#include <iostream>
#include <cmath>
#include <map>

using namespace std;

int main(){
	const int max_a = 10;
	const int max_b = 10;
	map <unsigned long long int, bool> powers;

	for(int itr_a = 2; itr_a <= max_a; ++itr_a){
		unsigned long long int tracker = itr_a;
		for(int itr_b = 2; itr_b <= max_b; ++itr_b){
			tracker *= itr_a;
			powers[tracker] = true;
		}
	}

	cout << "answer: " << powers.size() << endl;
}
