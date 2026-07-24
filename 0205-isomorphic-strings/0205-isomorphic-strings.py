class Solution(object):
    def isIsomorphic(self, s, t):
        # s and t have the same length
        s_size = len(s)
        dictionary_s = {}
        dictionary_t = {}
        for i in range(s_size):
            s_char = s[i]
            t_char = t[i]

            if s_char in dictionary_s and dictionary_s[s_char] != t_char:
                return False
            
            if t_char in dictionary_t and dictionary_t[t_char] != s_char:
                return False

            dictionary_s[s_char] = t_char
            dictionary_t[t_char] = s_char

            
        return True
            

        
        