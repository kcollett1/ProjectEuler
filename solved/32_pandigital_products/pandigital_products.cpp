#include <iostream>
#include <map>

using namespace std;

int calcdigits(int a){
	int numdigits = 0;
	while(a > 0){
		a /= 10;
		++numdigits;
	}
	return numdigits;
}

bool pandigital(int a, int b, int c){
	if(calcdigits(a) + calcdigits(b) + calcdigits(c) != 9) return false; // overkill with this particular script since I'm already ensuring they total 9 digits

	bool onethroughnine[10] = {true,false,false,false,false,false,false,false,false,false};

	while(a > 0){
		if(onethroughnine[a % 10]) return false;
		onethroughnine[a % 10] = true;
		a /= 10;
	}
	while(b > 0){
		if(onethroughnine[b % 10]) return false;
		onethroughnine[b % 10] = true;
		b /= 10;
	}
	while(c > 0){
		if(onethroughnine[c % 10]) return false;
		onethroughnine[c % 10] = true;
		c /= 10;
	}

	return true;
}

int main(){
	const int start_a[2] = {2,12};
	const int start_b[2] = {1234,123};
	const int end_a[2] = {8,81};
	const int end_b[2] = {4987,832};
	int pan_sum = 0;

	map <int, bool> valid;
	map <int, bool> used;

// check nums first for any 0 digits or any repeating digits
	bool onethroughnine[10] = {true,false,false,false,false,false,false,false,false,false};
	for(int itr = 0; itr < 2; ++itr){
		for(int itr_a = start_a[itr]; itr_a <= end_a[itr]; ++itr_a){
			onethroughnine[0] = true;
		       	for(int i = 1; i < 10; ++i) onethroughnine[i] = false;

			int tmp = itr_a;
			while(tmp > 0){
				if(onethroughnine[tmp % 10]){
					valid[itr_a] = false;
					break;
				}
				onethroughnine[tmp % 10] = true;
				tmp /= 10;
			}
		}

		for(int itr_b = start_b[itr]; itr_b <= end_b[itr]; ++itr_b){
			onethroughnine[0] = true;
		       	for(int i = 1; i < 10; ++i) onethroughnine[i] = false;

			int tmp = itr_b;
			while(tmp > 0){
				if(onethroughnine[tmp % 10]){
					valid[itr_b] = false;
					break;
				}
				onethroughnine[tmp % 10] = true;
				tmp /= 10;
			}
		}
	}

// now multiply all possibilities and check
	for(int itr = 0; itr < 2; ++itr){
		for(int itr_a = start_a[itr]; itr_a <= end_a[itr]; ++itr_a){
			if(valid.count(itr_a) > 0) continue;

			for(int itr_b = start_b[itr]; itr_b <= end_b[itr]; ++itr_b){
				int prod = itr_a * itr_b;

// we must have a total of 5 digits - but some combinations will be too large
				if(calcdigits(prod) > 4) break;

				if(valid.count(itr_b) > 0) continue;

				if(pandigital(itr_a, itr_b, prod)){
					if(used.count(prod) <= 0)
						{ pan_sum += prod; used[prod] = true; }
				}
			}
		}
	}

	cout << "answer: " << pan_sum << endl;
}
