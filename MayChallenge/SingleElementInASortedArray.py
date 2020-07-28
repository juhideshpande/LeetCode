class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        first,last=0,len(nums)-1
        mid = (first+last)//2
        if(last==0):
            return nums[0]
        elif(nums[0]!=nums[1]):
            return nums[0]
        elif(nums[last]!=nums[last-1]):
            return nums[last]
        else:
            while(first<=last):
                #print(first,last,mid)
                if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
                    # print("In if")
                    return(nums[mid])
                    break
                elif((nums[mid]==nums[mid-1] and mid%2!=0) or (nums[mid]==nums[mid+1] and mid%2==0)):
                    # print("In 2nd if",first,last)
                    first=mid+1
    
                else:
                    # print("in else",first,last)
                    last=mid-1
    
                mid = first + ((last-first) // 2)
