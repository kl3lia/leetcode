def subarraySum(nums, k):
    """
    :param nums: List[int]
    :param k: int
    :return: int
    """
    sum_map = {}
    sum_map[0] = 1 #special case
    count = curr_sum = 0
    for num in nums:
        curr_sum += num

        # Check if sum - k in hash
        count += sum_map.get(curr_sum - k, 0)

        # add curr_sum to hash
        sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
    return count


if __name__ == '__main__':
    #print(subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))
    #print(subarraySum([1], 0))
    #print(subarraySum([1, 0, 2, 4], 6)) #sum-k e.g 7-6=1, counted twice
    print(subarraySum([0, 0, 0], 0))

