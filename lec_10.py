nums = [1,2,4,8,1,6,9,6,4,4,1,2,8,3]
hash_map = {}
n = len(nums)
for i in range (n):
                    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
                    print(nums[i])