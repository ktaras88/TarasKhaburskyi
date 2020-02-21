def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count = 0
    summ = 0
    for i in arr:
        if i > 0:
            count +=1
        elif i < 0:
            summ += i
    return [count, summ]
    
print(count_positives_sum_negatives([1,2,3,4,5,-9,-8,-7]))