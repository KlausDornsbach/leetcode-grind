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
            c = s2[r]
            if c in s1_dic:
                s1_dic[c] -= 1
                if s1_dic[c] >= 0:
                    tot_found += 1
            
            if r - l >= s1_len:
                if s2[l] in s1_dic:
                    if s1_dic[s2[l]] >= 0:
                        tot_found -= 1
                    
                    s1_dic[s2[l]] += 1
                    
                l+=1
            
            if tot_found == s1_len:
                return True
            
            r+=1
        
        return False