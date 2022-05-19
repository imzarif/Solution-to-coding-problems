def MergeasaortedArray(nums1, nums2, m, n):
    for i in range(m,len(nums1)):
        nums1[i] = nums2[i-m]


    return nums1

    for j in range(1,len(nums1)):
        key = nums1[j]
        i = j-1
        while i>=0 and nums1[i]>key:
            nums1[i+1] = nums1[i]
            i-=1
        nums1[i+1] = key

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(MergeasaortedArray(nums1, nums2, m, n))
