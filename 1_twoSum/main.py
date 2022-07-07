class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}
        for i in range(len(nums)):

            if diff.get(nums[i]) == None:
                diff[nums[i]] = []

            diff[nums[i]].append(i)

            if diff.get(target - num) != None:
                if diff.get(target - num) != diff.get(num):
                    return [diff.get(num)[0], diff.get(target - num)[0]]
                elif len(diff.get(num)) > 1:
                    return [diff.get(num)[0], diff.get(num)[1]]