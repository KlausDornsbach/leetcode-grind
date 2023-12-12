class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        biggest = 0
        s = set(nums)
        for n in nums:
            if (n-1) not in s:
                curr = 1
                tmp = n+1
                while tmp in s:
                    curr += 1
                    tmp += 1

                if curr > biggest:
                    biggest = curr

        return biggest