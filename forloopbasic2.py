#1 output [-1, "big", "big", -5]
def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

print(biggie_size([-1,3,5,-5]))

#2 output [-1, 1, 1, 3] [1, 6, -4, -7, 2]
def count_positives(lst):
    count = 0
    for val in lst:
        if val > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -7, -2]))

#3 output 10, 7
def sum_total(lst):
    total = 0
    for val in lst:
        total += val
    return total

print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))

#4 output 2.5
def average(lst):
    total = 0
    for val in lst:
        total += val
    
    return float(total) / float(len(lst))

print(average([1 ,2 ,3 , 4]))

#5 output 4, 0
def length(lst):
    count = 0
    for val in lst:
        count += 1
    return count

print(length([37, 2, 1, -9]))
print(length([]))

#6 output 9, false
def minimum(lst):
    if len(lst) == 0:
        return False
    result = lst[0]
    for val in lst:
        if val < result:
            result = val
    return result

print(minimum([37, 2, 1, -9]))
print(minimum([]))

#7 output 37, false
def maximum(lst):
    if len(lst) == 0:
        return False

    result = lst[0]
    for val in lst:
        if val > result:
            result = val
    return result

print(maximum([37, 2, 1, -9]))
print(maximum([]))

#8 output {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}
def ultimate_analysis(lst):
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = lst[0]
        result['minimum'] = lst[0]
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(lst)

    return result

print(ultimate_analysis([37, 2, 1, -9]))
print(ultimate_analysis([]))

#9 output [-9, 1, 2, 37] [5, -9, 1, 2, 37] [] [1] [2, 1]
def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

print(reverse_list([37, 2, 1, -9]))
print(reverse_list([37, 2, 1, -9, 5]))
print(reverse_list([]))
print(reverse_list([1]))
print(reverse_list([1, 2]))