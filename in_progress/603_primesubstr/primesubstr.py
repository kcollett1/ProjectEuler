def isprime(i):
    for j in range(3,int(i**0.5)+1,2):
        if i%j==0: return False    
    return True

num = 19; stop = 10**6
nums = [2,3,5,7,11,13,17]
while len(nums) < stop:
    if isprime(num): nums.append(num)
    num += 2
