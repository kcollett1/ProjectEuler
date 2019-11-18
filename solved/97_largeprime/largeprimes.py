ans = '2'

for i in range(7830456): ans = str(int(ans) * 2)[-10:]

print('answer:', int(str(int(ans) * 28433)[-10:]) + 1)
