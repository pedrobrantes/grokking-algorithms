from typing import List, Optional

def binary_search(list_data: List[int], item: int) -> Optional[int]:
    """
    Performs a binary search on a sorted list to find the index of a specific item.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        list_data (List[int]): A sorted list of integers.
        item (int): The item to search for.

    Returns:
        Optional[int]: The index of the item if found, otherwise None.
    """
    low = 0
    high = len(list_data) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_data[mid]
        
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            
    return None
