
# 2. Reverse an Array
# Problem: Reverse the elements of a list in-place.

arr = [1, 2, 3, 4]
arr.reverse()  # or arr = arr[::-1]
print(arr)     # [4, 3, 2, 1]
# In arr[::-1]:
# start = empty → start from the end of the list by default because of negative step
# stop = empty → go until the beginning
# step = -1 → move backwards one step at a time
# Variants: Reverse without using built-ins.

# 3. Remove Duplicates
# Problem: Given a list, return a new list with duplicates removed.
arr = [1, 2, 2, 3, 4, 4, 4, 5, 2]
no_dupes = list(set(arr))  # Order may not be preserved
print(no_dupes)
#Follow-up: Maintain order without using set.
def uniq(input_arr):
    res1 = []
    for i in input_arr:
        if i not in res1:
            res1.append(i)
        else:
            res1.remove(i)
            res1.append(i)
    return res1


result = []
for x in arr:
    if x not in result:
        result.append(x)

# 4. sliding window, sum of subsets 
input22 = [2,4,3,6,8,9,1]
num = 17
def window_func(arr):
    size = len(arr)
    sum_r = 0
    for window_size in range(1, size):
        for i in range(0, size-window_size+1):
            sum_r = sum(arr[i:i+window_size])

            if sum_r == 17:
                good_wondow = arr[i:i+window_size]

    return good_wondow

print(window_func(input22))
