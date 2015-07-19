sum=2
first,second=1,2
while second+first<4000000:
    first,second=second,second+first
    if second % 2 == 0:
        sum += second
print("Answer: "+str(sum))#+" and total: "+str(total)