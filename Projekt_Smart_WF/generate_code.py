import random

def plus_or_minus_rnd(number, start=1, stop=10):
    curr_rnd = random.randrange(start, stop)
    rndit = random.randrange(0,2)
    if rndit == 1:
        return number + curr_rnd
    else: 
        return  number - curr_rnd
    


tmp = [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
tmp.sort()
print(tmp)
new_li = []
for i in tmp:
    op = plus_or_minus_rnd(i, 0, 100)

    new_li.append(op)
    
print(new_li)