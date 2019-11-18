with open('base_exp.txt','r') as fileo: lines = fileo.readlines()

for pair in lines:
    pair = [int(i) for i in pair.strip().split(',')]
    print(pair)
