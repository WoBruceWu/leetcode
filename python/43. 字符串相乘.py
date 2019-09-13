class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0 for _ in range(m+n)]
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                bit_mul = res[i+j+1] + int(num1[i])*int(num2[j])
                res[i+j+1] = bit_mul % 10
                res[i+j] += bit_mul//10
        idx = 0
        res = [str(ch) for ch in res]
        while idx < m+n and res[idx] == '0': idx += 1
        if idx == m+n: return '0'
        else: return ''.join(res[idx:])