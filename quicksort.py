import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data,colourArray(len(data), head , tail, border, border) )
    time.sleep(timeTick)

    for j in range(head, tail):
        if(data[j]<pivot):
            drawData(data,colourArray(len(data), head , tail, border, j, True) )
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border+=1

        drawData(data,colourArray(len(data), head , tail, border, j) )
        time.sleep(timeTick)


    drawData(data,colourArray(len(data), head , tail, border, tail, True) )
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail :
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        quick_sort(data, partitionIdx+1,tail, drawData, timeTick)


def colourArray(dataLen, head,tail, border, currIdx, isSwapping = False):
    colourArray = []
    for i in range(dataLen):

        if i>=head and i<= tail:
            colourArray.append("gray")
        else:
            colourArray.append("white")



        if i==tail:
            colourArray[i] == "orange"
        elif i == border:
            colourArray[i] == "red"
        elif i == currIdx:
            colourArray[i] == "yellow"


        if isSwapping:
            if i == border or i == currIdx:
                colourArray[i] = "green"
    return colourArray

    
    
