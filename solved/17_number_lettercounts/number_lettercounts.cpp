#include <iostream>

using namespace std;

int main(){
	const int one = 3;
	const int two = 3;
	const int three = 5;
	const int four = 4;
	const int five = 4;
	const int six = 3;
	const int seven = 5;
	const int eight = 5;
	const int nine = 4;
	const int ten = 3;
	const int eleven = 6;
	const int twelve = 6;
	const int thirteen = 8;
	const int fourteen = 8;
	const int fifteen = 7;
	const int sixteen = 7;
	const int seventeen = 9;
	const int eighteen = 8;
	const int nineteen = 8;
	const int twenty = 6;
	const int thirty = 6;
	const int forty = 5;
	const int fifty = 5;
	const int sixty = 5;
	const int seventy = 7;
	const int eighty = 6;
	const int ninety = 6;
	const int hundred = 7;
	const int and_let = 3;
	const int thousand = 8;

// 1 - 99: (9) 1-9; (1) 10; (1) 11-19; (10) 20, 30, 40, 50, 60, 70, 80, 90
	const int one_to_9 = one + two + three + four + five + six + seven + eight + nine;
	const int one_to_99 = ten + (one_to_9*9) + eleven + twelve + thirteen + fourteen + fifteen
		        + sixteen + seventeen + eighteen + nineteen
			+ 10*(twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety);
// 100 - 199: (100) 1, hundred; (99) and; (1-99 again)
// 200 - 299: (100) 2, hundred; (99) and; (1-99 again)
// 300 - 399: (100) 3, hundred; (99) and; (1-99 again)
// 400 - 499: (100) 4, hundred; (99) and; (1-99 again)
// 500 - 599: (100) 5, hundred; (99) and; (1-99 again)
// 600 - 699: (100) 6, hundred; (99) and; (1-99 again)
// 700 - 799: (100) 7, hundred; (99) and; (1-99 again)
// 800 - 899: (100) 8, hundred; (99) and; (1-99 again)
// 900 - 999: (100) 9, hundred; (99) and; (1-99 again)
// 1000: (1) one, thousand

// calculate:
// (1 - 99) 10x
// (and) (891)x
// (hundred) 900x
// (1-9) 100x
// (1) 1x
// (thousand) 1x

	const int ctr = (10*one_to_99) + (and_let*891) + (hundred*900) + (one_to_9*100) + one + thousand;
	cout << "the number of letters in 1-1000 spelled out are: " << ctr << endl;
}
