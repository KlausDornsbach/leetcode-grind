class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashSet = set()
        l, best = 0, 0
        for r in range(len(s)):
            if s[r] not in hashSet:
                hashSet.add(s[r])
                
            else:
                tmp =len(hashSet)
                if tmp > best:
                    best = tmp
                while s[r] in hashSet:
                    hashSet.remove(s[l])
                    l += 1
                hashSet.add(s[r])

        return best if len(hashSet) < best else len(hashSet)
            