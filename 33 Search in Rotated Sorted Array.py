class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        
        if not A:
            return -1
        
        start = 0
        end = len(A) -1
        
        while start < end -1:
            mid = start + (end-start)/2
            if A[mid] == target:
                return mid
            
            if A[start] < A[end]:
                if A[mid] < target:
                    start = mid
                else:
                    end = mid
            else:
                if (A[mid] < target and (A[mid] > A[start] or target <= A[start])) or (A[mid] > target and (A[mid] > A[start] and target <= A[end])):
                    start = mid
                else:
                    end = mid
        
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        
        return -1
