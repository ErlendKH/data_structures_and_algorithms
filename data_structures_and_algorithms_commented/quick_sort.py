
# 
def swap(my_list, index1, index2):
    # storing value of index1 in temp
    temp = my_list[index1]
    # setting value of index1 to be the value of index2
    my_list[index1] = my_list[index2]
    # setting value of index2 to be the value of index1 (temp)
    my_list[index2] = temp

# pivot index = 0
# end_index = length - 1
# last index of the list's length, so length - 1.
def pivot(my_list, pivot_index, end_index):

    swap_index = pivot_index

    # Hm. From 1 up to but not included end_index+1.
    for i in range(pivot_index+1, end_index+1):

        if my_list[i] < my_list[pivot_index]:
            # set swap_index forward by 1 index.
            swap_index += 1
            # swap items at i and swap index.
            swap(my_list, swap_index, i)
    
    # Finally, swap the values of swap_index with the final
    # pivot_index.
    swap(my_list, pivot_index, swap_index)
        
    return swap_index

###

# So in the example:
# left = 0
# right = 6 (length of list - 1)
def quick_sort_helper(my_list, left, right):

    # Debug:
    # print('quick_sort | left: ', left)
    # print('quick_sort | right: ', right)

    if left < right:
        # Getting the index of the pivot
        pivot_index = pivot(my_list, left, right)

        # Note: Not including the pivot_index itself, because
        # it's already in the correct position.
        # pivot_index-1
        quick_sort_helper(my_list, left, pivot_index-1)
        # pivot_index+1
        quick_sort_helper(my_list, pivot_index+1, right)
    
    return my_list

# For not needing to pass beginning and end index
def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort([4,6,1,7,3,2,5])) # [1, 2, 3, 4, 5, 6, 7]

# So, based on the printed debug messages of pivot and quick_sort:

# Initial quick_sort_helper([list], 0, 6):

# quick_sort | left:  0
# quick_sort | right:  6
# pivot | pivot_index:  0
# pivot | end_index:  6
# pivot | swap_index:  3

# So it quick sorts the left side first.
# index 0 to 2:

# quick_sort | left:  0
# quick_sort | right:  2
# pivot | pivot_index:  0
# pivot | end_index:  2
# pivot | swap_index:  1

# Here, left is not less than right, so left side is done.

# quick_sort | left:  0
# quick_sort | right:  0
# quick_sort | left:  2
# quick_sort | right:  2

# Quick-sorting the right side -- index 4 to 6:

# quick_sort | left:  4
# quick_sort | right:  6
# pivot | pivot_index:  4
# pivot | end_index:  6
# pivot | swap_index:  5

# This time, left is not less than right on the right side
# of the pivot, so this breaks the second recursion.

# quick_sort | left:  4
# quick_sort | right:  4
# quick_sort | left:  6
# quick_sort | right:  6

# Finally, the sorted list is returned.

# [1, 2, 3, 4, 5, 6, 7]
