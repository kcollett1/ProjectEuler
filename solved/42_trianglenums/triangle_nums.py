#!/usr/bin/env python

file = open('p042_words.txt')
wordlist = file.readlines()
file.close()
wordlist = wordlist[0].split('","')
wordlist[0], wordlist[-1] = wordlist[0][1:], wordlist[-1][:-1]

for i in range(len(wordlist)):
	ans = 0
	for let in wordlist[i].lower():
		ans += ord(let) - 96
	wordlist[i] = ans
wordlist = sorted(wordlist)

trinum = 1; trictr = 1; numtriwords = 0
for num in wordlist:
	while trinum < num:
		trictr += 1
		trinum = trictr*(trictr+1)/2
	if trinum == num:
		numtriwords += 1

print 'ans = ',numtriwords
