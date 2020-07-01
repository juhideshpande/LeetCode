class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        boards=["abcde","fghij","klmno","pqrst","uvwxy","z"]
        new_dict={}
        h=[0,0]
        ans=""
        for i in range(len(boards)):
            for j in range(len(boards[i])):
                new_dict[boards[i][j]]= [i,j]
        start=new_dict['a']
        #s=start
        for i in target:
            s=start
            temp=new_dict[i]
            h[0]=temp[0]-s[0]
            h[1]=temp[1]-s[1]
            if h[1]<0:
                ans+=abs(h[1])*"L"
            if h[0]<0:
                #print(i,h[0],"if h0")
                ans+=abs(h[0])*"U"
            if h[0]>0:
                #print(i,h[0],"else h0")
                ans+=abs(h[0])*"D"            
            
            if h[1]>0:
                ans+=abs(h[1])*"R" 
                
            ans+="!"    
            start=new_dict[i]
                
            
           
        return ans

