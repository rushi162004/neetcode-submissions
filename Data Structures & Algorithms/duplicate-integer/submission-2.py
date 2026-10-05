class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        if len(nums) < 0 or len(nums) > 10**5:
            return False
        else:
            for num in nums:
                if num in seen and (num >=10**-9 or num<= 10**9):
                    return True
                else:
                    seen.add(num)
            return False

        