def fourSum( nums):# -> List[List[int]]:
    nums.sort()
    res= []
    for i in range(len(nums)-3):
        if i>0 and nums[i] == nums[i+1]:
            continue
        for j in range(i+1,len(nums)-3):
            k = j+1
            l = len(nums)-1
            
            while(k<l):
                foursum = nums[i]+nums[j]+nums[k]+nums[l]
                if foursum > 0:
                    l = l-1
                elif foursum < 0 :
                    k = k+1
                else:
                    res.append([nums[i],nums[j],nums[k],nums[l]])
                    k = k+1
                    while(nums[k]==nums[k+1]):
                        k == k+1
                    while(nums[l]==nums[l-1]):
                        l = l-1
                    k = k+1
                    l = l-1
                           # k+=1
    return res







print(fourSum([1,0,-1,0,-2,2]))