import math
value=int(600851475143)
endCicle=int(math.floor(math.sqrt(value)))#600851475143
primers=[2]

def messageProgress():
    global value
    print("Max next primer: " + str(math.sqrt(value)))

def checkForPrime():
    global value 
    lastPrimer = primers[len(primers)-1]
    while True:
        if value % lastPrimer == 0:
            value /= lastPrimer
            print("Found primer: "+str(int(lastPrimer))+" new value: "+str(int(value)))
        else:
            return

def findNextPrime():
    nextPrime = primers[len(primers)-1] + 1
    maxNextPrime = math.sqrt(nextPrime)
    ok = True
    while True:   
        for pos in primers:
            if nextPrime % pos == 0 and pos <= maxNextPrime:
                ok = False
                break
        if ok == True:
            primers.append(nextPrime)
            #print(str(nextPrime))
            return
        nextPrime += 1
        maxNextPrime = math.ceil(math.sqrt(nextPrime))
        ok = True

if value > 1:
    while True:
        checkForPrime()
        if value == 1:
            break
        findNextPrime()

