def square_of_sum(numRange):
    sum = 0
    for num in range(1, numRange+1):
        sum += num
    return sum**2


def sum_of_squares(numRange):
    sum = 0
    for num in range(1, numRange+1):
        sum += num**2
    return sum

def difference(numRange):
    return square_of_sum(numRange) - sum_of_squares(numRange)
