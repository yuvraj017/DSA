def findUnion1(arr1, arr2):
    """
    Finds the union of two arrays using a dictionary to track the frequency of elements.
    Each unique element from both arrays is added to the union list.

    Steps:
    1. Iterate through `arr1` and add elements to a frequency dictionary.
    2. Repeat the process for `arr2`.
    3. Extract all keys from the frequency dictionary and append them to the union list.
    4. Return the union list.

    :param arr1: First input array.
    :param arr2: Second input array.
    :return: List containing the union of the two arrays.
    """
    freq_dict = {}
    union = []
    for num in arr1:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    for num in arr2:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    for num in freq_dict:
        union.append(num)

    return union

def findUnion2(arr1, arr2):
    """
    Finds the union of two arrays using Python's set operations.
    Combines the elements of both arrays into a set to ensure uniqueness.

    Steps:
    1. Convert `arr1` and `arr2` into sets.
    2. Perform a union operation on the two sets.
    3. Convert the resulting set back into a list.
    4. Return the union list.

    :param arr1: First input array.
    :param arr2: Second input array.
    :return: List containing the union of the two arrays.
    """
    return list(set(arr1) | set(arr2))

def findUnion3(arr1, arr2):
    """
    Finds the union of two arrays using the two-pointer technique.
    Assumes the arrays are sorted or sorts them before processing.

    Steps:
    1. Sort both input arrays.
    2. Use two pointers to traverse both arrays simultaneously.
    3. Compare elements at the pointers:
       - Add the smaller element to the union list and move the pointer.
       - If elements are equal, add one to the union list and move both pointers.
    4. Append remaining elements from either array to the union list.
    5. Return the union list.

    :param arr1: First input array.
    :param arr2: Second input array.
    :return: List containing the union of the two arrays.
    """
    arr1.sort()
    arr2.sort()
    i, j = 0, 0
    union = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        union.append(arr1[i])
        i += 1

    while j < len(arr2):
        union.append(arr2[j])
        j += 1

    return union


arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]

print(findUnion1(arr1, arr2))
