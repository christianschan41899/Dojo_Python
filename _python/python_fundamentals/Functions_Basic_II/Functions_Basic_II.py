#Countdown
def countdown(num):
    for i in range(num, -1, -1):
        print(i)

countdown(10)

#print and return
def printAndReturn(list):
    print(list[0])
    return list[1]

print(printAndReturn([1,2]))

#first plus length
def plusLength(list):
    return (list[0] + len(list))

print(plusLength([1,2,3,4,5]))

#greater than second
def greaterthanSecond(list):
    newList = []
    count = 0
    for i in list:
        if i>list[1]:
            newList.append(i)
            count += 1

    if(len(newList)<2):
        return False
    else:
        print(f"{count} numbers greater than the second value")
        return newList

print(greaterthanSecond([1,2,4,5,2,4,7,9]))
print(greaterthanSecond([1,8,3,4,10]))

#This Length, That Value

def lengthyValue(length, value):
    newList = []
    for i in range(0, length):
        newList.append(value)
    return newList

print(lengthyValue(7, 7))
        