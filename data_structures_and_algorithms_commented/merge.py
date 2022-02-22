
def merge(list1, list2):
    combined = []

    # Need to use while loops.

    i = 0
    j = 0

    # Running while loop until either i or j is equal to their
    # respective lists.
    while i < len(list1) and j < len(list2):
        # Adding the lowest number to the combined list.

        # If value of index i is less than value of index j:
        # (Note: What if there are duplicate values? ...)
        if list1[i] < list2[j]:
            combined.append(list1[i])
            # 
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    # Doing checks for both lists to add remaining items.
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

print(merge([1,2,7,8], [3,4,5,6])) # [1, 2, 3, 4, 5, 6, 7, 8]

