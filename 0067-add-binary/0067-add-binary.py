class Solution(object):
    def addBinary(self, a, b):
        string = []
        indexA, indexB, carry = len(a) - 1, len(b) - 1, 0
        while indexA >= 0 or indexB >= 0 or carry == 1:
            if indexA >= 0:
                carry += int(a[indexA])
                indexA -= 1
            if indexB >= 0:
                carry += int(b[indexB])
                indexB -= 1
            
            string.append(str(carry % 2))
            carry //= 2
        return "".join(string[::-1])