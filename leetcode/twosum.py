class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1

        while i < j:
            sum = nums[i] + nums[j]

            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [nums[i],nums[j]]

        return []


arr = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(arr,target))