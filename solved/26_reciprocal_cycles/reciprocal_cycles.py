maxrecur = 0; maxdiv = 0

for div in range(1,1000):
    num = 10; used = []; digs = 1
    while digs <= 5000:
        digs += 1
        j = float(num)/float(div)
        if j%1 == 0: break
        used.append(int(j))
        num = (num%div)*10
    pattern = False; cyc = 0
    while 25+3*cyc < len(used) and not pattern:
        cyc += 1
        if used[25:25+cyc] == used[25+cyc:25+2*cyc] == used[25+2*cyc:25+3*cyc]:
            pattern = True
            if maxrecur < cyc: maxrecur = cyc; maxdiv = div

print maxrecur,maxdiv
