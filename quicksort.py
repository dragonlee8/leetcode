def quicksort(nums, start, end):
    if start >= end:
        return

    pivot = nums[(start + end)/2]
    left = start
    right = end
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        quicksort(nums, start, right)
        quicksort(nums, left, end)



nums = [2,3,12,5,6,2,7,7,8,8,9]
quicksort(nums, 0, len(nums)-1)
print nums
