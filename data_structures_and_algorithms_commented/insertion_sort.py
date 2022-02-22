
def insertion_sort(my_list):
    for i in range(1, len(my_list)):

        # 
        temp = my_list[i]
        # The item before index i.
        j = i-1

        # If temp(i) is less than value of j.
        # j > -1 to prevent the index from being -1 after j -= 1.
        while temp < my_list[j] and j > -1:
            # Doing a swap here:

            # Ok, so setting index i the value of index j.
            my_list[j+1] = my_list[j]
            # Then, set index j the value of i.
            my_list[j] = temp

            j -= 1
        
    return my_list

print(insertion_sort([4,2,6,5,1,3])) # [1, 2, 3, 4, 5, 6]