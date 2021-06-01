class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;

        for(int i=0;i<nums.length;i++){
            int base = 10;
            int digit = 1;
            while(true){
                if(nums[i]/base == 0){
                    break;
                }else{
                    digit++;
                }
                base *= 10;
            }
            if(digit%2==0){
                count++;
            }
        }
        return count;
    }
}

/*
Runtime: 1 ms, faster than 95.43% of Java online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 39.1 MB, less than 100.00% of Java online submissions for Find Numbers with Even Number of Digits.
 */