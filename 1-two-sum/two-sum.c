int* twoSum(int* nums, int numsSize, int target, int* returnSize){
     int *k =(int*) calloc(2,sizeof(int));
    * returnSize = 2;
     int n = numsSize;
        for (int i = 0; i < n ;  i++) {
          int x = target - nums[i];
            for (int j = i + 1; j < n; j++) {
              if (x == nums[j])
              {
                k[0] = j;
                k[1] = i;
              }
            }
        }
        return k;
}