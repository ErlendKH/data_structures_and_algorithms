
def bubble_sort(my_list):
    # starts at: length of my_list - 1
    # stops at 0.
    # -1 --> backwards loop ...
    # Ex. 5, 4, 3, 2, 1, 0
    for i in range(len(my_list) - 1, 0, -1):
        # Comparisons in this loop: (this one is going forward)
        for j in range(i):
            # if item is greater than the next item:
            if my_list[j] > my_list[j+1]:

                # temporary storing first item
                temp = my_list[j]
                # Giving first item the value of the second item
                my_list[j] = my_list[j+1]
                # Then, giving second item the value of first item
                my_list[j+1] = temp

    return my_list

print(bubble_sort([4,2,6,5,1,3])) # [1, 2, 3, 4, 5, 6]