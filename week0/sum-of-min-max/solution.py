def sum_of_min_and_max(lst):
    minimal = min(lst)
    maximal = max(lst)
    suma = minimal + maximal
    
    return suma

print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
print(sum_of_min_and_max([-10,5,10,100]))
print(sum_of_min_and_max([1]))
