'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''


        
def sort(l,i,r):
        while i<=r:
            if list[i]==0:
               list[i],list[l]=list[l],list[i]
               l+=1
               i+=1
            elif list[i]==1:
                 i+=1
            elif list[i]==2:
                 list[i],list[r]=list[r],list[i]
                 r-=1
        return list
list=list(map(int,input().split(",")))
res=sort(0,0,len(list)-1)
print(res)


'''without functions'''

list=list(map(int,input().split(",")))
l=0
i=0
r=len(list)-1
while i<=r:
    if list[i]==0:
        list[i],list[l]=list[l],list[i]
        l+=1
        i+=1
    elif list[i]==1:
          i+=1
    elif list[i]==2:
          list[i],list[r]=list[r],list[i]
          r-=1
print(list)



class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        l=0
        i=0
        r=len(nums)-1
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                i+=1
            elif nums[i]==1:
                i+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1

        




