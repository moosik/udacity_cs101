def check_sudoku(ll):
    rowLength = len(ll[0])
    for el in ll:
        for i in range(1,rowLength+1):
            print i
            if i not in el:
                return False
                break
    i = 0
    for el in ll[0]:
        for subList in ll[1:]:
            if subList[i] == el:
                return False
                break
        i = i+1
    return True

