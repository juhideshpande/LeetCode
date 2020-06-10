class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        for i in range(len(address)):
            if(address[i]=="."):
                return address.replace(".","[.]")
               
        
