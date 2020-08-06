class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        rptr, wptr = 0, 0
        while rptr < len(chars):
            ch, f = chars[rptr], 0
            while rptr < len(chars) and chars[rptr] == ch:
                rptr = rptr+1 
                f=f+1
            chars[wptr] = ch
            wptr=wptr + 1
           # print(wptr,chars[wptr])
            if f > 1:
                for c in str(f): # for digits greater than 9
                    chars[wptr]=c
                    print(wptr)
                    wptr = wptr + 1
        return wptr       
