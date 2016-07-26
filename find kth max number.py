class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A:
            return None
        
        if len(A) == 1:
            return A[0]
        
        mid = len(A) /2 
        start = 0 
        end = len(A) - 1
        pivot = A[mid]
        while start <= end:
            while start <= end and A[start] > pivot:
                start += 1
            while start <= end and A[end] < pivot:
                end -= 1
            
            if start <= end:
                A[start] , A[end] = A[end], A[start]
                start += 1
                end -= 1
            
        #print k, start, A, pivot
        if end > 0 and k <= end + 1:
            return self.kthLargestElement(k, A[:end+1])
        elif start < len(A) and k > start:
            return self.kthLargestElement(k-start, A[start:])
        return A[k-1]
