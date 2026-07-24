class Solution(object):
    def romanToInt(self, s):
        # Assign dictionary for Roman numerals
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M": 1000}
        num = 0
        length = len(s)

        # Iterate through string. Assign current letter
        # and assign next value so long as not going out of 
        # bounds. If the next letter is greater than the 
        # current one, say current is I and next is X, then
        # subtract from num, so subtract 1. Then, on the next
        # iteration, if current is greater than next, then we 
        # add 10, which total would net +9, which makes sense.
        # Otherwise, say next is greater, like L, then
        # subtract 10. Assuming L is the last one, then add
        # 50 to num. Net total is -1-10+50 = 39
        for i in range(length):
            current = roman[s[i]]
            if i + 1 < length:
                next_val = roman[s[i + 1]]
            else:
                next_val = 0
            
            if current < next_val:
                num = num - current
            else:
                num = num + current
        return num
        