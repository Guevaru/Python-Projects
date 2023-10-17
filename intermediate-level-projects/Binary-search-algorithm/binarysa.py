def binary_search(a_list, an_item):
    # Binary search to find an_item in a_list (non-recursive)
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item:
            return True  # Item found
        elif an_item < a_list[mid_point]:
            last = mid_point - 1  # Adjust the search range
        else:
            first = mid_point + 1  # Adjust the search range
    return False  # Item not found

def binary_search_rec(a_list, first, last, an_item):
    # Binary search to find an_item in a_list (recursive)
    if first <= last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item:
            return True  # Item found
        elif an_item < a_list[mid_point]:
            return binary_search_rec(a_list, first, mid_point - 1, an_item)
        else:
            return binary_search_rec(a_list, mid_point + 1, last, an_item)
    return False  # Item not found

def interactive_binary_search(a_list):
    # Perform binary search based on user input
    item = int(input("Enter the number you want to search for: "))
    found = binary_search(a_list, item)
    if found:
        print(f"{item} found in the list.")
    else:
        print(f"{item} not found in the list.")

if __name__ == '__main__':
    a_list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]
    
    print('Binary Search (Iterative):', binary_search(a_list, 4))
    print('Binary Search (Recursive):', binary_search_rec(a_list, 0, len(a_list) - 1, 4))

    interactive_binary_search(a_list)
