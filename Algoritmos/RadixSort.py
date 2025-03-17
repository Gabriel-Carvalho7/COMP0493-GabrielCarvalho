def radixSort(array):
    def countingDigit(array, digit):
        count = [0] * 10 
        output = [0] * len(array)
        
        for num in array:
            d = (num // (10 ** digit)) % 10
            count[d] += 1
        
        for i in range(1, 10):
            count[i] += count[i-1]
        
        for num in reversed(array):
            d = (num // (10 ** digit)) % 10
            output[count[d] - 1] = num
            count[d] -= 1
        
        return output
    
    def radixPositive(array, maxValue):
        if not array:
            return []
        maxDigit = 0
        current = maxValue

        while current > 0:
            maxDigit += 1
            current = current // 10
            
        for digit in range(maxDigit):
            array = countingDigit(array, digit)
        return array
    
    if not array:
        return []
    
    negatives = [x for x in array if x < 0]
    positives = [x for x in array if x >= 0]
    
    sortNegatives = []
    if negatives:
        maxNeg = max(-x for x in negatives)
        sortNegatives = radixPositive([-x for x in negatives], maxNeg)
        sortNegatives = [-x for x in reversed(sortNegatives)]
    
    sortPositives = []
    if positives:
        maxPos = max(positives)
        sortPositives = radixPositive(positives, maxPos)
    
    return sortNegatives + sortPositives

if __name__ == "__main__":
    array = [4, 2, -1, 0, 3, -2, 170, 45, 75, 90, 802, 24, 2, 66]
    print(f"\nRadixSort: {radixSort(array)}\n")