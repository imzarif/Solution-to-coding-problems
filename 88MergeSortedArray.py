def merge(nums1, m, nums2, n):
    count = 0
    for i in range(m,m+n):
        nums1[i] = nums2[count]
        count+=1



    for j in range(1, len(nums1)):
        key = nums1[j]
        for i in range(j-1,-1,-1):
            if nums1[i]>key:
                nums1[i+1] = nums1[i]
                nums1[i] = key
            else:
                nums1[i+1] = key
                break


    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1, 3, nums2, 3))