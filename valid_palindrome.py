class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        actual_s = ''.join(filter(str.isalnum, str(s))).lower()
        i = 0
        j = len(actual_s)-1
        while j > i:
            if actual_s[i] != actual_s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True