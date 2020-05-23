my_list = [["1", "3", "5"],
           ["2", ["3", ["2", "4", [[["2", "1"], "5"], "3"], "5"], "1"]]]

my_list_int = [[1, 3, 5],
               [2, [3, [2, 4, [[[2, 1], 5], (1, 2)], {5000, 10000}], 1]]]


def flatten(xs):
    result = []
    if isinstance(xs, (list, tuple, set)):
        for x in xs:
            result.extend(flatten(x))
    else:
        result.append(xs)
    return result


print(flatten(my_list), "\n\n", flatten(my_list_int))
