#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int alph_num(char character){
	if(character == 'a' || character == 'A') return 1;
	else if(character == 'b' || character == 'B') return 2;
	else if(character == 'c' || character == 'C') return 3;
	else if(character == 'd' || character == 'D') return 4;
	else if(character == 'e' || character == 'E') return 5;
	else if(character == 'f' || character == 'F') return 6;
	else if(character == 'g' || character == 'G') return 7;
	else if(character == 'h' || character == 'H') return 8;
	else if(character == 'i' || character == 'I') return 9;
	else if(character == 'j' || character == 'J') return 10;
	else if(character == 'k' || character == 'K') return 11;
	else if(character == 'l' || character == 'L') return 12;
	else if(character == 'm' || character == 'M') return 13;
	else if(character == 'n' || character == 'N') return 14;
	else if(character == 'o' || character == 'O') return 15;
	else if(character == 'p' || character == 'P') return 16;
	else if(character == 'q' || character == 'Q') return 17;
	else if(character == 'r' || character == 'R') return 18;
	else if(character == 's' || character == 'S') return 19;
	else if(character == 't' || character == 'T') return 20;
	else if(character == 'u' || character == 'U') return 21;
	else if(character == 'v' || character == 'V') return 22;
	else if(character == 'w' || character == 'W') return 23;
	else if(character == 'x' || character == 'X') return 24;
	else if(character == 'y' || character == 'Y') return 25;
	else if(character == 'z' || character == 'Z') return 26;
	else return -1;
}

int alph_val(string a){
	int sumval = 0;

	for(int i = 0; i < a.length(); ++i)
		sumval += alph_num(a[i]);

	return sumval;
}

int alph_less_equal_greater(string a, string b){
// 0 --> less than
// 1 --> equal to
// 2 --> greater than
	if(a == b) return 1; // a equal b

	int len = a.length();
	if(b.length() < len) len = b.length();

	int itr = 0;
	while( ( alph_num(a[itr]) == alph_num(b[itr]) ) && ( itr < (len - 1) ) ){ ++itr; }

	if( alph_num(a[itr]) == alph_num(b[itr]) ){
		if(a.length() > b.length()) return 2; // a greater than b
		else return 0; // a less than b
	}else if( alph_num(a[itr]) < alph_num(b[itr]) ){ return 0; // a less than b
	}else if( alph_num(a[itr]) > alph_num(b[itr]) ){ return 2; } // a greater than b

	return -1;
}

void quicksort_alph(string* names_arr, int first_ind, int last_ind){
	if(last_ind - first_ind < 1) return; // already sorted, array of 1 (or 0)

// pick pivot: middle, round down (first + ((last-first)/2)) more correct for large array sizes to avoid overflow in indices
	int pivot_ind = (last_ind + first_ind) / 2;

// partition:
	// swap the pivot to the beginning to iterate through the rest
	// (sometimes pivot may already be at beginning,
	// but more efficient to be redundant sometimes than to check every time)
	string pivot_name = names_arr[pivot_ind];
	names_arr[pivot_ind] = names_arr[first_ind];

	// now iterate, moving when necessary
	int i = first_ind + 1;
	int j = last_ind;
	while(i <= j){
		while(i <= j &&
		      alph_less_equal_greater(names_arr[i],pivot_name) < 2) // less or equal
			++i;

		while(i <= j &&
		      alph_less_equal_greater(names_arr[j],pivot_name) == 2) // greater
			--j;

		if(i < j){
			// swap the names in i and j
			string tempname = names_arr[i];
			names_arr[i] = names_arr[j];
			names_arr[j] = tempname;
		}
	}
	// put the pivot in it's final position
	names_arr[first_ind] = names_arr[i - 1];
	names_arr[i - 1] = pivot_name; // this is the final position
				       // will need to sort above and
				       // below this point recursively now

	// call sort for subarrays, to recursively sort
	quicksort_alph(names_arr, first_ind, i - 2);
	quicksort_alph(names_arr, i, last_ind);

	return;
}

int main(){
	string names[5163];
	unsigned long int running_sum = 0;

	string line = "";
	ifstream namefile("names.txt");

	if(namefile.is_open()){
// reading the file, storing in a string variable
		namefile >> line;
		namefile.close();

// parse the names and store in string array
		string temp = "";
		int num_name = 0;
// start at first letter of first name
		for(int i = 1; i < line.size(); ++i){
			if(line[i] == '"'){ // we've  finished recording name
				names[num_name] = temp;
				temp = "";
				i += 2;
				++num_name;
			}else temp += line[i];
		} // now all names are stored in a string array

// sort them into alphabetical order
		quicksort_alph(names,0,5162);

// now calculate running_sum of all alphabetical values
		for(int i = 0; i < 5163; ++i){ running_sum += ((i + 1) * alph_val(names[i])); }

		cout << "total of all name scores: " << running_sum << endl;

	}else cout << "Error: unable to open file" << endl;

	return 0;
}
