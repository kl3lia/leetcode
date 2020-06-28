import collections


def three_sum_brute_force(nums):
    res = []
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    partial_res = sorted([nums[i], nums[j], nums[k]])
                    if partial_res not in res:
                        res.append(partial_res)
    return res


def three_sum_hash(nums):
    """
    ??? WHY DOES NOT WORKK!?
    :param nums:
    :return:
    """
    counter = collections.Counter(nums)
    store = set()
    res = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            x = -(nums[i] + nums[j])
            if x in store:
                print(x, nums[i], nums[j])
                temp = sorted([x, nums[i], nums[j]])
                temp_count = collections.Counter(temp)
                condition = all(temp_count.get(key) <= counter.get(key) for key in temp)
                if temp not in res and condition:
                    res.append(temp)
            else:
                store.add(nums[i])
    return res


def threeSum(self, nums):
    res = []
    nums.sort()
    ls = len(nums)
    for i in range(ls - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = ls - 1
        while j < k:
            curr = nums[i] + nums[j] + nums[k]
            if curr == 0:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif curr < 0:
                j += 1
            else:
                k -= 1
    return res


if __name__ == '__main__':
    print(three_sum([3, 0, -2, -1, 1, 2]))
