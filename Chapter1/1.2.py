def drop_first_last(grades):
    first, *middle, last = grades
    return middle


print(drop_first_last([1, 2, 23, 323, 24]))
