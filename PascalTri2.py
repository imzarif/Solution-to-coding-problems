def PascalTriangletwo(rowIndex):
    numRows = rowIndex+1
    mainList = [[1], [1, 1]]
    if numRows == 1 or numRows == 2:
        return mainList[numRows-1]
    tempList = []
    count = 1  # keeps track of parent of temp  list
    nextCount = count + 1  # iterates through temp list
    while count < numRows - 1:
        prevList = mainList[count]
        for i in range(nextCount + 1):
            if i == 0 or i == nextCount:
                tempList.append(1)
            else:
                tempList.append(prevList[i - 1] + prevList[i])

        mainList.append(tempList)
        tempList = []
        count += 1
        nextCount += 1

    return mainList [rowIndex]


print(PascalTriangletwo(3))