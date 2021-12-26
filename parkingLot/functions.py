# Returns element closest to target in arr[]
def find_nearest_lot(arr, n, target):
    """
    The goal is to traverse through the given array and keep track of absolute differenceof current element with every element.
    Finally return the element that has minimum absolution difference.
    :param arr: list of available slots
    :param n: length of available slots
    :param target: entry slot
    :return: element that has minimum absolute difference
    """
    #[2,5,6,7,9,11,15]
    # Corner cases
    if target <= arr[0]:
        return arr[0]
    if target >= arr[n - 1]:
        return arr[n - 1]

    # Doing binary search
    i, j, mid = 0, n, 0

    while i < j:
        mid = (i + j) // 2

        if arr[mid] == target:
            return arr[mid]

        # If target is less than array
        # element, then search in left
        if target < arr[mid]:

            # If target is greater than previous
            # to mid, return closest of two
            if mid > 0 and target > arr[mid - 1]:
                return compare_closest(arr[mid - 1], arr[mid], target)

            # Repeat for left half
            j = mid

        # If target is greater than mid
        else:
            if mid < n - 1 and target < arr[mid + 1]:
                return compare_closest(arr[mid], arr[mid + 1], target)

            # update i
            i = mid + 1

    # Only single element left after search
    return arr[mid]


def compare_closest(val1, val2, target):
    """
    # Method to compare which one is the more close.
    # We find the closest by taking the difference
    # between the target and both values. It assumes
    # that val2 is greater than val1 and target lies
    # between these two.
    """
    if target - val1 >= val2 - target:
        return val2
    else:
        return val1
