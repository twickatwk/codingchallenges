
# Write a function that merges two sorted arrays into array1
# Time: O(n) | Space: O(1)
def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return nums1
        
        results = []
        a_idx = 0
        b_idx = 0
        
        while a_idx < m and b_idx < n:
            if nums1[a_idx] <= nums2[b_idx]:
                results.append(nums1[a_idx])
                a_idx += 1
            else:
                results.append(nums2[b_idx])
                b_idx += 1
        
        while a_idx < m:
            results.append(nums1[a_idx])
            a_idx += 1
        while b_idx < n:
            results.append(nums2[b_idx])
            b_idx += 1
        
        for i in range(m+n):
            nums1[i] = results[i]