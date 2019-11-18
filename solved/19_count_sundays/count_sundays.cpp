#include <iostream>

using namespace std;

// given a current day, month, and year
// set day and return to 0-6 for what day of the week the next month starts on
int after_this_month(int& day, int month, int year){
	int num_days = 31; // how many days in the month
	if(month == 3 || month == 5 || month == 8 || month == 10) num_days = 30;
	else if(month == 1){
		if((year%4) == 0){
			if((year%100) == 0 && (year%400) != 0) num_days = 28;
			else num_days = 29;
		}else num_days = 28;
	}
	// how many days is the next day offset by
	// if 28 --> first day of next month doesn't change
	if(num_days == 29) day = (day + 1)%7;
	else if(num_days == 30) day = (day + 2)%7;
	else if(num_days == 31) day = (day + 3)%7;
	return day;
}

// count the number of first sundays between: jan 1, 1901 (tuesday) - dec 31, 2000
// september 1, 1901 (sunday) - first first sunday!
// october 1, 2000 (sunday) - last first sunday!
int main(){
	int day = 2; // start jan 1, 1901 on a tuesday
	int first_sundays = 0;
	for(int year = 1901; year <= 2000; ++year){
		for(int month = 0; month < 12; ++month){
			if( after_this_month(day, month, year) == 0 ) ++first_sundays;
		}
	}

	cout << endl << "    The number of sundays falling on the first day of the month"
		     << " in the twentieth century is " << first_sundays << endl << endl;
}
