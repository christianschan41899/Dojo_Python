def BubbleSort(list):
    for j in range(len(list)-1, 0, -1): #Start at length of list minus 1 to prevent out of bound, stop at 0 which will be when the sort finishes, count down
        for i in range(j): #j will loop i as just 1 short of as many times as list has indexes, and i will loop through a shorter and shorter number of indexes determined by j's increment
            if(list[i]>list[i+1]): #check for if the current index is larger than its index
                list[i], list[i+1] = list[i+1], list[i] #if so, swap values
    return list

print(BubbleSort([1,0,4,5,3,2,7,6,8]))