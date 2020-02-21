def solution(number):
    list1 = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list1.append(i)
    return sum(list1)