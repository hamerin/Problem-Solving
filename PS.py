l=[1,1];exec('l.append(l[-1]+l[-2]);'*80);n=int(input());print((l[n]+l[n-1])*2)