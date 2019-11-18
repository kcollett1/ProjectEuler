#include <iostream>

using namespace std;

unsigned long long int step(unsigned long long int curr_right, unsigned long long int curr_down,
	 const int dimension, unsigned long long int memo[]){

	// check if we reached the edge of the square and only one path remains
	if( curr_right == dimension || curr_down == dimension )
		return 1;

	// check if step(m,n) was already iterated, if so, use result instead of recalculating result
	if(memo[curr_right + (curr_down*dimension)] != 0)
		return memo[curr_right + (curr_down*dimension)];

	// increment right first then down
	memo[curr_right + (curr_down*dimension)] = step(curr_right + 1, curr_down, dimension, memo)
		                                 + step(curr_right, curr_down + 1, dimension, memo);

	return memo[curr_right + (curr_down*dimension)];
}

int main(){
	unsigned long long int right = 0, down = 0;
	int dimension; // check how many paths of an N x N square
	cout << endl << "    dimension: ";
	cin >> dimension;

	unsigned long long int memo[dimension*dimension]; // to memoize results to avoid recalculating
	for(int i = 0; i < dimension*dimension; ++i) memo[i] = 0;

	cout << "Number of paths possible through a " << dimension
	     << " by " << dimension << " square is "
	     << step(right, down, dimension, memo) << endl;
}
