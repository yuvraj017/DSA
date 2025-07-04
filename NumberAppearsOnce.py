def number_appears_once1(nums):
    """
    This function takes a list of integers where every integer appears twice except for one.
    It returns the integer that appears only once.

    :param nums: List[int] - List of integers
    :return: int - The integer that appears only once
    """
    result = 0
    for num in nums:
        result ^= num
    return result

def number_appears_once2(nums):
    """
    This function takes a list of integers where every integer appears twice except for one.
    It returns the integer that appears only once using a set to track seen numbers.

    :param nums: List[int] - List of integers
    :return: int - The integer that appears only once
    """
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    for num, count in freq_dict.items():
        if count == 1:
            return num

    return None  # In case no unique number is found, though the problem guarantees one exists.

def number_appears_once3(nums):
    """
    This function takes a list of integers where every integer appears twice except for one.
    It returns the integer that appears only once using a set to track seen numbers.

    :param nums: List[int] - List of integers
    :return: int - The integer that appears only once
    """
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)

    return seen.pop() if seen else None  # Return the unique number or None if not found.

# Example usage:
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(number_appears_once1(nums))  # Output: 4
    print(number_appears_once2(nums))  # Output: 4
    print(number_appears_once3(nums))  # Output: 4