def counting_sort(arr):
    if not arr:
        return []
    
    minValue = min(arr)
    maxValue = max(arr)
    
    range_of_elements = maxValue - minValue + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    for num in arr:
        count[num - minValue] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for num in reversed(arr):
        output[count[num - minValue] - 1] = num
        count[num - minValue] -= 1
    
    return output

if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print(f"\nCountingSort: {counting_sort(arr)}\n") 