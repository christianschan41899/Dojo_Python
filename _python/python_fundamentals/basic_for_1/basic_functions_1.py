#Basic
def basic():
    for i in range(0, 151):
        print(i)

basic()

#Multiples of 5

def multiplesOfFive():
    for i in range(5, 101, 5):
        print(i)

multiplesOfFive()

#Counting the Dojo Way

def DojoCounting():
    for i in range(1, 101):
        if(i%10 == 0):
            print("Coding Dojo")
        elif(i%5 == 0):
            print("Coding")
        else:
            print(i)

DojoCounting()

#That sucker's huge

def hugeCount():
    sum = 0
    for i in range(1, 500001):
        if(i%2 != 0):
            sum += i
    print(sum)

hugeCount()

#Countdown by fours

def downFour():
    for i in range(2018, 0, -4):
        print(i)

downFour()

#Flexible Count

def flexibleCount(lowNum, highNum, multi):
    for i in range(lowNum, highNum+1):
        if(i%multi == 0):
            print(i)

flexibleCount(2, 9, 3)
