#Biggie Size
def posToBig(lst):
    for i in range(len(lst)):
        if(lst[i]>0):
            lst[i]='big'
    return lst

print(posToBig([-5,4,-8,-4,3,6]))

#count positives

def countPositives(lst):
    count = 0
    for i in lst:
        if(i>0):
            count+=1
    lst[len(lst)-1] = count
    return lst

print(countPositives([1, 4, -7, 8, -2, -1]))

#Sum total
def sumTotal(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sumTotal([1, 2, 5, 7, 10]))

#Average
def average(lst):
    sum = 0
    for i in lst:
        sum += i
    return (sum/len(lst))

print(average([1,5,6,9]))

#length
def length(lst):
    count = 0
    for i in lst:
        count += 1
    return count

print(length([1,2,4,5,9]))
print(length([]))

#Minimum
def minimum(lst):
    if(len(lst) == 0):
        return False
    else:
        min = lst[0]
        for i in lst:
            if(i<min):
                min = i
        return min

print(minimum([1, 5, -7, 3, 4]))
print(minimum([]))

#Maximum
def maximum(lst):
    if(len(lst) == 0):
        return False
    else:
        max = lst[0]
        for i in lst:
            if(i>max):
                max = i
        return max

print(maximum([1, 5, -7, 3, 4]))
print(maximum([]))

#Ultimate Analyst
def ultimateAnalyst(lst):
    analysis = {}
    sum = 0
    for i in lst:
        sum += i
    analysis.update({"sumTotal": sum})

    average = sum / len(lst)
    analysis.update({"Average": average})

    min= 0
    if(len(lst) == 0):
        min= False
    else:
        min = lst[0]
        for i in lst:
            if(i<min):
                min = i
    analysis.update({"Minimum": min})

    max = 0
    if(len(lst) == 0):
        max=False
    else:
        max = lst[0]
        for i in lst:
            if(i>max):
                max = i
    analysis.update({"Maximum": max})

    count = 0
    for i in lst:
        count += 1
    analysis.update({"Length": count})
    return analysis

print(ultimateAnalyst([1,4,7,8,-7,9,-1]))

#Reverse
def reverse(lst):
    halfLength=int(len(lst)/2)
    for i in range(halfLength):
        temp = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = lst[i]
        lst[i] = temp
    return lst

print(reverse([1,2,5,7,8,6]))


