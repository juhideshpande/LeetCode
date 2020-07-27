class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        a=[]
        for i in range(len(S)):
            if(S[i]!="#"):
                a.append(S[i])
            else:
                if not a:
                    i+=1
                else:
                    a.pop(-1)
                    i+=1
        print (a)
        str(a)
        b=[]
        for i in range(len(T)):
            if(T[i]!="#"):
                b.append(T[i])
            else:
                if not b:
                    i += 1
                else:
                    b.pop(-1)
                    i += 1
        print (b)
        str(b)
       # print(a.sort())
       # print(b.sort())
        if a==b:
            return True
        else:
            return False

        
