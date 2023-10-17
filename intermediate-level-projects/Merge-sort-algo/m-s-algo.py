def merge_sort(a_list):
    # Merge Sort algorithm
    if len(a_list) > 1:
        mid_point = len(a_list) // 2
        left_half = a_list[:mid_point]
        right_half = a_list[mid_point:]

        # Recursively sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        # Merge the sorted halves back into the original list
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1

def display_merge_sort(a_list):
    # Display the process of merge sort
    print("Original List:", a_list)
    merge_sort(a_list)
    print("Sorted List:", a_list)

if __name__ == '__main__':
    a_list = [45, 7, 85, 24, 60, 25, 38, 63, 1]
    display_merge_sort(a_list)
