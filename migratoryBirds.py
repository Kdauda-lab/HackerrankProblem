def migratoryBirds(arr):

    """A program to check the frequency of the occurrence of a number in a list and
    return the min of the number with the highest value """

    li = []
    set_value = set(arr)
    di = {item: 0 for item in set_value}
    for i in di.keys():
        for j in arr:
            if i == j:
                di[i] += 1
    max_value = max(di.values())

    for key, value in di.items():
        if value == max_value:
            li.append(key)
    sorted(li)
    return li[0]


migratoryBirds([2,2,3,1,1])