from typing import List, Optional

def binary_search(list_data: List[int], item: int) -> Optional[int]:
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

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    
    result = binary_search(my_list, target)
    
    print(f"List: {my_list}")
    print(f"Target: {target}")
    
    if result is not None:
        print(f"Item found at index: {result}")
    else:
        print("Item not found.")
