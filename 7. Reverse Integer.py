class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            n = str(x)[1:]
        else:
            n = str(x)

        n = int(n[::-1])

        maxint32 = 2147483647
        if n > maxint32:
            return 0
        
        return n if x >= 0 else n * (-1)

print Solution().reverse(10000003)