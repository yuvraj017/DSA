from typing import List

def searchInARotatedSortedArrayII(arr: List[int], k: int) -> bool:
    """
    Search target k in rotated sorted array arr that may contain duplicates.
    Returns True if found, False otherwise.
    """

    n = len(arr)
    if n == 0:
        return False

    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # Direct hit
        if arr[mid] == k:
            return True

        # Ambiguous case due to duplicates:
        # cannot decide which side is sorted when low, mid, high are equal.
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # If left half is sorted
        if arr[low] <= arr[mid]:
            # If target lies within sorted left half
            if arr[low] <= k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half must be sorted
            if arr[mid] < k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


# Example usage / quick tests
if __name__ == "__main__":
    cases = [
        ([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 3, True),
        ([2,5,6,0,0,1,2], 0, True),
        ([2,5,6,0,0,1,2], 3, False),
        ([1,1,3,1], 3, True),   # tricky duplicate case
        ([], 1, False),
    ]

    for arr, k, expected in cases:
        ans = searchInARotatedSortedArrayII(arr, k)
        print(f"{arr}  k={k} -> {ans}")
