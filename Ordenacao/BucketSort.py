def bucketSort(array, qtdeBuckets=None):
    if not array:
        return []
    
    minValue = min(array)
    maxValue = max(array)

    if minValue == maxValue:
        return array.copy()

    if qtdeBuckets is None:
        qtdeBuckets = len(array)
    qtdeBuckets = max(1, qtdeBuckets)

    buckets = [[] for _ in range(qtdeBuckets)]
    bucketRange = (maxValue - minValue) / qtdeBuckets 

    for num in array:
        index = int((num - minValue) / bucketRange)
        index = min(index, qtdeBuckets - 1) 
        buckets[index].append(num)

    sortedArray = []
    for bucket in buckets:
        sortedArray.extend(sorted(bucket)) 

    return sortedArray

if __name__ == "__main__":
    array = [4, 2, 2, 8, 3, 3, 1]
    print(f"\nBucketSort: {bucketSort(array)}\n")
