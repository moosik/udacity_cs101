def quicksort(l):
    result=[]
    if len(l)==1 or len(l)==0:
        return l
    else:
        pivot = l[0]
        rightSide = []
        leftSide = []
        for i in range(1,len(l)):
            if l[i]<pivot:
                rightSide.append(l[i])
            else:
                leftSide.append(l[i])
        sortedRight = quicksort(rightSide)
        sortedLeft = quicksort(leftSide)
    result+=sortedRight
    result.append(pivot)
    result+=sortedLeft
    return result
