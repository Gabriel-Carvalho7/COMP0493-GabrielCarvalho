def InversionIndex(array):
    def mergeSortCount(array):
        if len(array) <= 1:
            return array, 0
        
        mid = len(array) // 2
        left, leftInv = mergeSortCount(array[:mid])
        right, rightInv = mergeSortCount(array[mid:])
        merged, splitInv = mergeCount(left, right)
        
        totalInv = leftInv + rightInv + splitInv
        return merged, totalInv
    
    def mergeCount(left, right):
        merged = []
        i = j = splitInv = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                splitInv += len(left) - i 
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, splitInv
    
    _, inversions = mergeSortCount(array)
    return inversions

if __name__ == "__main__":
    array = [2, 4, 1, 3, 5]
    print(f"\nNúmero de inversões: {InversionIndex(array)}\n") 