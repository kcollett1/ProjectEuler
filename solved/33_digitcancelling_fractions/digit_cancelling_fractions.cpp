#include <iostream>

using namespace std;

int main(){
	int running_num = 1, running_denom = 1;

	for(int denom = 11; denom < 100; ++denom){
		int denom_d2 = denom % 10;
		if(denom_d2 == 0) continue;
		int denom_d1 = (denom / 10) % 10;

		for(int num = 10; num < denom; ++num){
			int num_d2 = num % 10;
			if(num_d2 == 0) continue;
			int num_d1 = (num / 10) % 10;

			if(num_d1 == denom_d1){
				if(num_d2*denom == num*denom_d2){
					running_num *= num_d2;
					running_denom *= denom_d2;
					cout << num_d2 << '/' << denom_d2 << " ...... "
					     << num << '/' << denom << " ...... "
   					     << running_num << '/' << running_denom << endl;
				}
				continue;
			}
			if(num_d1 == denom_d2){
				if(num_d2*denom == num*denom_d1){
					running_num *= num_d2;
					running_denom *= denom_d1;
					cout << num_d2 << '/' << denom_d1 << " ...... "
					     << num << '/' << denom << " ...... "
					     << running_num << '/' << running_denom << endl;
				}
				continue;
			}
			if(num_d2 == denom_d1){
				if(num_d1*denom == num*denom_d2){
					running_num *= num_d1;
					running_denom *= denom_d2;
					cout << num_d1 << '/' << denom_d2 << " ...... "
					     << num << '/' << denom << " ...... "
					     << running_num << '/' << running_denom << endl;
				}
				continue;
			}
			if(num_d2 == denom_d2){
				if(num_d1*denom == num*denom_d1){
					running_num *= num_d1;
					running_denom *= denom_d1;
					cout << num_d1 << '/' << denom_d1 << " ...... "
					     << num << '/' << denom << " ...... "
					     << running_num << '/' << running_denom << endl;
				}
				continue;
			}
		}
	}

	cout << "done with loop... " << running_num << '/' << running_denom << endl;
}
