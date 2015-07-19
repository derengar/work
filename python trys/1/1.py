sum=0
total=0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        sum+=i;
        total+=1
print("Sum of elements: "+str(sum)+", and total numbers: "+str(total))