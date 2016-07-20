def merge(nums1, nums2):
	ret = []
	idx1 = idx2 = 0
	while idx1 <len(nums1) and idx2 < len(nums2):
		if nums1[idx1] < nums2[idx2]:
			ret.append(nums1[idx1])
			idx1 += 1
		else:
			ret.append(nums2[idx1])
			idx2 += 1
		
	if idx1 != len(nums1):
		for i in range(idx1, len(nums1)):
			ret.append(nums1[i])
	else:
		for i in range(idx2, len(nums2)):
			ret.append(nums2[i])
	return ret
	
def mergesort(nums):
	if not nums or len(nums) <= 1:
		return nums
		
	mid = (len(nums))/2
	
	return merge(mergesort(nums[:mid]), mergesort(nums[mid:]))



nums = [2,3,12,5,6,2,7,7,8,8,9]
print mergesort(nums)
