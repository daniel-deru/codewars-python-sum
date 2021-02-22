def two_sum(numbers, target):
    for i in range(len(numbers)):
        test = numbers[i]
        for j in range(len(numbers)):
            if test + numbers[j] == target:
                if i is not j:
                    return (i, j)


print(two_sum([1,2,3], 4))