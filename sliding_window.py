class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_dic = {}
        

        # initialize the dict
        for c in s1:
            if c not in s1_dic:
                s1_dic[c] = 0
            
            s1_dic[c] += 1

        tot_found = 0
        s1_len = len(s1)
        l = 0
        r = 0

        while r < len(s2):
            curr_char = s2[r]
            if curr_char in s1_dic:
                if s1_dic[curr_char] > 0:
                    tot_found += 1
                    if tot_found == s1_len:
                        return True
                    
                    s1_dic[curr_char] -= 1
                else:
                    while s2[l] != s2[r]:
                        s1_dic[s2[l]] += 1
                        tot_found -= 1
                        l += 1
                    l+=1
            
            else:
                while l <= r:
                    if s2[l] in s1_dic:
                        s1_dic[s2[l]] += 1
                        tot_found -= 1
                
                    l += 1
            
            r += 1

