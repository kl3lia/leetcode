def two_sum(nums, target):
    """
    :param nums: List[int]
    :param target:  int
    :return: List[int]
    """
    store = {}
    for idx, num in enumerate(nums):

        if target - num in store:

            return [ store.get(target - num), idx]
        else:
            store[num] = idx
    return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
