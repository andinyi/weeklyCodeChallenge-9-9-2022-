def largestGap(inputArray):
    inputArray = sorted(inputArray)
    return (abs(inputArray[0] - inputArray[-1]))

print(largestGap([-3, -1, 6, 7, 0]))