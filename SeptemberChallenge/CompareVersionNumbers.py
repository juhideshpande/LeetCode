class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        
        while version1_list or version2_list:
            if version1_list:
                num1 = int( version1_list.pop( 0 ) )
            else:
                num1 = 0
            if version2_list:
                num2 = int( version2_list.pop( 0 ) )
            else:
                num2 = 0
            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
        return 0
