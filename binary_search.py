class Solution(object):

    # recursive just with value

    # def find(self, nums, target):
    #     pivot = nums[(len(nums)-1) // 2]
    #     if len(nums) == 1 and target != pivot:
    #         return -1
    #
    #     if target == pivot:
    #         return pivot
    #     elif target > pivot:
    #         return self.find(nums[(len(nums) // 2) + 1:], target)
    #     else:  # target < pivot
    #         return self.find(nums[:(len(nums) // 2)], target)

    # recursive with index (gets a bit clunky)

    # def find(self, nums, start, end, target):
    #     pivot_idx = (end - start) // 2 + start
    #     pivot = nums[pivot_idx]
    #     if target == pivot:
    #         return pivot_idx
    #     else:
    #         if start == end:
    #             return -1
    #         else:
    #             if target > pivot:
    #                 return self.find(nums, min(pivot_idx + 1, len(nums)), end,  target)
    #             else:  # target < pivot
    #                 return self.find(nums, start, max(pivot_idx - 1, 0), target)

    # iterative (Two Pointers) with index
    def find(self, nums, target):
        start, end = 0, len(nums) - 1

        # protect pointers and go for it. When they 'break', it actually means target is just not there.
        while start <= end:
            pivot_idx = (end - start) // 2 + start
            if nums[pivot_idx] < target:
                start = pivot_idx + 1
            elif nums[pivot_idx] > target:
                end = pivot_idx - 1
            else:
                return pivot_idx
        return -1


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # return self.find(nums, 0, len(nums) - 1, target)
        return self.find(nums, target)

print(Solution().search([-1,0,3,5,9,12], 4))
# print(Solution().search([2, 5], 6))
