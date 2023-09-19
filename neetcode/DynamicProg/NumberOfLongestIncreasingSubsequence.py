nums = [1,3,5,4,7]
n = len(nums)
lsub = [1] * n
for i in range(n-1,-1,-1):
 for j in range(i+1,n,1):
  if (nums[i] < nums[j]):
   lsub[i] = max(lsub[i],1+lsub[j])

print(lsub)