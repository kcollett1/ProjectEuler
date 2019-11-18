#include <iostream>

using namespace std;

int main(){
// choose an N x N square to calculate the sum of the diagonals
// must be odd and greater than 1
	int dimension = 1001;
	int layers = (dimension - 1) / 2.; // calculate the layers to iterate through on the square
	int ctr = 1, tracker = 1, skip = 2;
	for( int start = 1; start <= layers; ++start, skip += 2 ){
		for(int i = 0; i < 4; ++i){
			tracker += skip;
			ctr += tracker;
		}
	}
	cout << endl << "Sum of the diagonals for a " << dimension
	     << " by " << dimension << " number spiral is " << ctr
	     << endl;
}
