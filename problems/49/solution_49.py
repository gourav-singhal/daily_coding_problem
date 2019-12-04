def coding_problem_49(arr):
    """
    Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
    For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
    42, 14, -5, and 86. Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any
    elements. Do this in O(N) time.
    Examples:

    >>> coding_problem_49([34, -50, 42, 14, -5, 86])
    137
    >>> coding_problem_49([-5, -1, -8, -9])
    0
    """
    cumulative_sum, cumulative_sums = 0, [0]
    for val in arr:
        cumulative_sum += val
        cumulative_sums.append(cumulative_sum)

    highest_peak, max_sum = cumulative_sums[-1], 0
    for index in range(len(cumulative_sums) - 1, 0, -1):
        highest_peak = max(highest_peak, cumulative_sums[index])
        max_sum = max(max_sum, highest_peak - cumulative_sums[index - 1])

    return max_sum


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
