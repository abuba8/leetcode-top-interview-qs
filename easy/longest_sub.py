def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return 0
        
        start = 0
        end = 0
        unique_chars = set()
        max_length = 0
        
        while end < len(s):
            if s[end] not in unique_chars:
                unique_chars.add(s[end])
                end+=1
                max_length = max(max_length, len(unique_chars))
            else:
                unique_chars.remove(s[start])
                start+=1
            
        return max_length