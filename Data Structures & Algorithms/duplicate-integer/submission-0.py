class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set() # 1, 2, 3
        for i in range(len(nums)):
            s.add(nums[i])

        lst_s = list(s) #[1, 2, 3]
        d = {} #{}
        for j in range(len(lst_s)):
            d[lst_s[j]] = 0 # {1:0, 2:0, 3:0}

        for k in range(len(nums)): 
            if d[nums[k]] < 1: #{1:1, 2:1, 3:1,}
                d[nums[k]] += 1

            else:
                return True
        return False