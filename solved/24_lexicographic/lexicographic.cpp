#include <iostream>

using namespace std;

// permutations of 0 1 2 3 4 5 6 7 8 9
// all permutations of numbers starting with 0: there are 9! = 362,880
// then all starting with 1: there are another 9!, so in total: 725,760
// then all starting with 2 goes over 1,000,000 so our number starts with 2
// if we have 2 and then 0, there are 8! = 40,320 possibilities, putting us at 766,080
// if we have 2 and then 1, another 8! possibilites, putting us at 806,400
// if we have 2 and then 3, another 8! possibilites, putting us at 846,720
// if we have 2 and then 4, another 8! possibilites, putting us at 887,040
// if we have 2 and then 5, another 8! possibilites, putting us at 927,360
// if we have 2 and then 6, another 8! possibilites, putting us at 967,680
// 2 and then 7 puts us over 1,000,000, so our number starts with 2 7
// if we have 2 7, then 0, there are 7! = 5,040 possibilities, putting us at 972,720
// if we have 2 7, then 1, another 7! possibilities, putting us at 977,760
// if we have 2 7, then 3, another 7! possibilities, putting us at 982,800
// if we have 2 7, then 4, another 7! possibilities, putting us at 987,840
// if we have 2 7, then 5, another 7! possibilities, putting us at 992,880
// if we have 2 7, then 6, another 7! possibilities, putting us at 997,920
// if we have 2 7, then 8, that puts us over 1,000,000, so our number starts with 2 7 8
// we have 2 7 8, then 0, then there are 6! = 720 possibilities of this, putting us at 998,640
// we have 2 7 8, then 1, another 6! possibilities, putting us at 999,360
// 2 7 8 3 puts us over 1,000,000 so our number starts with 2 7 8 3
// we have 2 7 8 3, then 0, there are 5! = 120 possbilities, putting us at 999,480
// we have 2 7 8 3, then 1, another 5! possbilities, putting us at 999,600
// we have 2 7 8 3, then 4, another 5! possbilities, putting us at 999,720
// we have 2 7 8 3, then 5, another 5! possbilities, putting us at 999,840
// we have 2 7 8 3, then 6, another 5! possbilities, putting us at 999,960
// we have 2 7 8 3, then 9, puts us over 1,000,000, so our number starts with 2 7 8 3 9
// we have 2 7 8 3 9, then 0, there are 4! = 24 possbilities, putting us at 999,984
// 2 7 8 3 9 1 puts us over 1,000,000, so our number starts with 2 7 8 3 9 1
// we have 2 7 8 3 9 1, then 0, there are 3! = 6 possibilities, putting us at 999,990
// we have 2 7 8 3 9 1, then 4, another 3! possibilities, putting us at 999,996
// 2 7 8 3 9 1 5 puts us over 1,000,000, so our number starts with 2 7 8 3 9 1 5
// we have 2 7 8 3 9 1 5, then 0, there are 2! = 2 possibilities, putting us at 999,998
// 2 7 8 3 9 1 5 4 (0 6) ... 999,999
// 2 7 8 3 9 1 5 4 (6 0) ... 1,000,000!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
