from typing import List, Optional, Tuple

def floor_index(arr: List[int], x: int) -> int:
    """Return index of floor(x) (largest index i such that arr[i] <= x), or -1 if none."""
    n = len(arr)
    low, high = 0, n - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            ans = mid            # mid is a candidate for floor
            low = mid + 1       # try to find a larger candidate on the right
        else:
            high = mid - 1
    return ans

def ceil_index(arr: List[int], x: int) -> int:
    """Return index of ceil(x) (smallest index i such that arr[i] >= x), or -1 if none."""
    n = len(arr)
    low, high = 0, n - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid           # mid is candidate for ceil
            high = mid - 1      # try to find smaller candidate on the left
        else:
            low = mid + 1
    return ans

def find_floor_and_ceil(arr: List[int], x: int) -> Tuple[Optional[int], Optional[int]]:
    """
    Return (floor_value, ceil_value). If floor/ceil doesn't exist, return None for that side.
    Works in O(log n).
    """
    fi = floor_index(arr, x)
    ci = ceil_index(arr, x)
    floor_val = arr[fi] if fi != -1 else None
    ceil_val  = arr[ci] if ci != -1 else None
    return floor_val, ceil_val

# Example
if __name__ == "__main__":
    arr = [3, 4, 4, 7, 8, 10]
    x = 5
    f, c = find_floor_and_ceil(arr, x)
    print("floor:", f, "ceil:", c)   # floor: 4 ceil: 7
