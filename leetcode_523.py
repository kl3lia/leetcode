def checkSubarraySum(nums, k):
    """
    :param nums: List[int]
    :param k: int
    :return: bool
    """
    curr_sum = 0
    store = {}
    store[0] = -1
    for idx, num in enumerate(nums):
        curr_sum += num
        if k != 0:
            curr_sum = curr_sum % k
        if curr_sum in store:
            if idx - store.get(curr_sum) >= 2:
                return True
        else:
            store[curr_sum] = idx





if __name__ == '__main__':
    print(checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(checkSubarraySum([0, 0], 0))
    print(checkSubarraySum([5, 0, 0], 0))
   # print(checkSubarraySum([23, 2, 4, 0, 0], 0))
    print(checkSubarraySum([0, 1, 0], 0))
    print(checkSubarraySum([1, 2, 3], 5))
