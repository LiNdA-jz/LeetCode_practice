from audioop import reverse


class Solution:
    def reverse(self, x: int) -> int:
        if (x>=0):
            intStr = str(x)
            rev = intStr[::-1]
            revInt = int(rev)
        else:
            x *= -1
            intStr = str(x)
            rev = intStr[::-1]
            rev = "-" + rev
            revInt = int(rev)

        if (revInt<-2**31 or revInt>2**31-1):
            return 0
        else:
            return revInt