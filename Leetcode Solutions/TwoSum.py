class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = []
        for i in range(len(nums)):
            compliment = target - nums[i]
            if nums[i] in hash_table:
                if nums[i] == compliment:
                    l = nums.index(nums[i])
                    nums.remove(nums[i])
                    nums.insert(0, 1111111110)
                    w = nums.index(compliment)
                    #return[]
                    return [l,w]
                else:
                    return [nums.index(nums[i]),nums.index(compliment)]
            else:
                hash_table.append(compliment)
 
