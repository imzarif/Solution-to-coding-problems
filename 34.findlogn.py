def searchRange(nums, target):
        indices = [-1, -1]
        first = 0
        last = len(nums) - 1


        while first <= last:
            middle = int((first + last) / 2)
            if nums[middle]==target:
                first_middle = middle
                last_middle = middle
                while last_middle<last and nums[last_middle]==target:
                    last_middle+=1

                while first_middle>first and nums[first_middle]==target:
                    first_middle-=1

                if nums[first_middle] != target:
                    indices.append(first_middle+1)
                else:
                    indices.append(first_middle)
                if nums[last_middle]!=target:
                    indices.append(last_middle-1)
                else:
                    indices.append(last_middle)

                return indices[2:len(indices)]

            if nums[middle] > target:
                last = middle - 1
            if nums[middle] < target:
                first = middle + 1

        return indices
nums =  [6]
target = 6
print(searchRange(nums, target))
