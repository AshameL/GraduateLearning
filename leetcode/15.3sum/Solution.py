class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort() #先进行排序
		rList = [] 
		for k in range(len(nums)):
			if nums[k] > 0:
				break;	#不需要从头循环到尾,避免重复。如果num[k]>0,则一定有重复的数据。
			if k>0 and nums[k]==nums[k-1]:#当前k与之前k-1进行去重的比较
				continue
			target = 0-nums[k]
			i=k+1
			j=len(nums)-1
			while i<j:
				if nums[i]+nums[j]==target:
					rList.append([nums[k],nums[i],nums[j]])
					while i<j and nums[i]==nums[i+1]:
						i = i + 1
					while i<j and nums[j]==nums[j-1]:
						j = j - 1
					i = i+1
					j=j-1
				elif nums[i]+nums[j]<target:
					i=i+1
				else:
					j=j-1
		return rList
if __name__=='__main__':
	nums = [-1,0,1,2,-1,-4]
	list = Solution().threeSum(nums)
	print(list)
					