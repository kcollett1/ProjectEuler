#include <iostream>
#include <cmath>
#include <math.h>

using namespace std;

/*
 * QUESTIONS FOR THIS PROBLEM:
 * does fc need to be integer as well? - assume it doesn't for now
 * does ab need to be less than ae as well? - assume it does for now

 * ab = height of rectangle
 * ae = width of rectangle
 * fc = perpendicular height of isosceles triangle
 *      must be greater than 0 and less than ab
 */

bool is_heron(const unsigned long long int ab,
	      const unsigned long long int ae,
	      const unsigned long long int bc){

	if(ab == 0 || ae == 0 || bc == 0) return false;
	if( ab > ae ) return false; // not sure about this one
	if( fmod(sqrt(ae*ae + ab*ab),1.) != 0 ) return false;

	unsigned long long double fc = 0.5 * sqrt(4*bc*bc - ae*ae);
	if( !(fc < ab && fc > 0) ) return false;
	if( fmod(sqrt(ae*ae + 4*fc*fc),2.) != 0 ) return false;
	if( fmod(sqrt(ae*ae + 4*(ab+fc)*(ab+fc)),2.) != 0 ) return false;
	return true;

// just assume you test integers only, so don't need this
	//if( fmod(ab,1.) != 0 || fmod(ae,1.) != 0 || fmod(bc,1.) != 0 ) return false;
}

unsigned long long int calc_perim_of_heron(const unsigned long long int ab,
		                           const unsigned long long int ae,
					   const unsigned long long int bc){
	if(is_heron(ab, ae, bc)) return ( 2*ab + ae + 2*bc ) ;
	else return 0;
}

unsigned long long int sum_all_heron_perims(const unsigned long long int perim){
	unsigned long long int perim_running_sum = 0;

	int ab = 161, ae = 240;
	double fc = 64.;
	if(is_heron(ab, ae, bc)){
		cout << "this is a heron envelope." << endl;
		cout << "perimeter = " << calc_perim(ab, ae, bc) << endl;
	}

	return perim_running_sum;
}

int main(){
	const unsigned long long int perim = 1000;
	//const unsigned long long int perim = 10000000;

	cout << "The sum of the perimeters of all heron envelopes with a perimeter"
	     << " less than or equal to " << perim << " is "
	     << sum_all_heron_perims(perim) << endl;

	return 0;
}
