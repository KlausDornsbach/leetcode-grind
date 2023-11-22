class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for s in strs:
            sorted_string = "".join(sorted(s))
            print(sorted_string)
            if sorted_string in d:
                d[sorted_string].append(s)
            else:
                d[sorted_string] = [s]
        
        return [string_list for string_list in d.values()]
