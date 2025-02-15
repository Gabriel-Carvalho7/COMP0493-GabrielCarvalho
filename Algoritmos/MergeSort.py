def mergeSort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = mergeSort(array[:mid]) 
    right = mergeSort(array[mid:])  
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

if __name__ == "__main__":
    array = [4, 2, -1, 0, 3, -2, 170, 45, 75, 90, 802, 24, 2, 66]
    print(f"\nMergeSort: {mergeSort(array)}\n")