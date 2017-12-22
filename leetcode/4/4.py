class Solution:
	def findKthSortedArrays(A,m,B,n,k):
		#java的参考https://www.cnblogs.com/duanqiong/p/4415049.html
		# c的参考 https://www.cnblogs.com/ganganloveu/p/4180523.html
		# 关键疑问在与如何计算边界值
		# make sure A is shorter than B
		if m>n:
			return findKthSortedArrays(B,n,A,m,k)
		# A is empty
		if m == 0:
			return B[k-1]
		# k==1(m>0 is guaranteed)
		if k ==1:
			return min(A[0],B[0])
			
		# main process
		''' Acandi Bcandi'''
		if (k-1)/2 >= m   #why (k-1)/2	?
			Acandi = A[m-1]
			Bcandi = B[k-m-1]
			if Acandi == Bcandi:
				return Acandi
			elif Acandi > Bcandi:
				#for A:no skip
				#for B:skip the k-m smaller elements(including Bcandi)
				return findKthSortedArrays(A,m,)
		
		
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        