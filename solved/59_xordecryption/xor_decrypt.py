i = 0
#d = [{},{},{}]
r = 0
#m = ''
#k = [101,120,112] #'exp'
k = [ord(j) for j in 'exp']

with open('p059_cipher.txt') as f:
    c = [int(j) for j in f.readlines()[0].split(',')]

for l in c:
#    if l in d[i]: d[i][l] += 1
#    else: d[i][l] = 1
    #m += chr(l ^ k[i])
    r += l ^ k[i]
    i = (i + 1) % 3

####################
#s = [list(reversed(sorted(j, key = j.get))) for j in d]
#for j in s:
#    print('set of chars in order of frequency:')
#    print([bin(l)[2:].zfill(8) for l in j])
####################
#print('space in ascii/bin = ', ord(' '),'/',bin(ord(' '))[2:].zfill(8))
#print(m)
####################
print('answer:', r)

# to decode this message I found the most common character in each set of every third character
# then xor'd that with the ord() value for the space character
# this gave me the key of 'exp'
# using this key I decoded the message by xor'ing all the values and printed the message
# and got a coherent english message!
# then we just go through the originial message and find a running sum of the ascii values
