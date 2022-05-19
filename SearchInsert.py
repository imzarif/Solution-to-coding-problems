def searchInsert(nums, target):
    first = 0
    last = len(nums) - 1
    # middle = int(len(nums)/2)
    # position = -1
    # print(nums[first],nums[middle],nums[last])
    found = False

    while found == False and first <= last:
        middle = int((first + last) / 2)

        if nums[middle] == target:
            found = True
            return middle

        elif nums[middle] > target:
            last = middle - 1

        elif nums[middle] < target:
            first = middle + 1

    return first


nums = [1]
print(searchInsert(nums, 2))