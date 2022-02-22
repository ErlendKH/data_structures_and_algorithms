
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

my_list = [4,6,1,7,3,2,5]

print(pivot(my_list, 0, 6)) # 3

print(my_list) # [2, 1, 3, 4, 6, 7, 5]