
def selection_sort(my_list):
    for i in range(len(my_list) - 1):

        min_index = i
        # starting at i+1 (indexes higher than min_index)
        # Up to but not including len(my_list).
        for j in range(i+1, len(my_list)):
            # If item j less than that of min_index ...
            if my_list[j] < my_list[min_index]:
                min_index = j
        
        # Check:
        if i != min_index:
            # Swapping the values of index i and index j
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    
    return my_list

print(selection_sort([4,2,6,5,1,3])) # [1, 2, 3, 4, 5, 6]