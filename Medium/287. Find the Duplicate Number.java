class Solution {
    public int findDuplicate(int[] nums) {
        int turtle = nums[0];
        int hare = nums[0];
        
        while(true){
            turtle = nums[turtle];
            hare = nums[nums[hare]];
            if(turtle == hare){break;}
        }
        
        int ptr1 = nums[0];
        int ptr2 = turtle;
        
        while(ptr1 != ptr2){
            ptr1 = nums[ptr1];
            ptr2 = nums[ptr2];
        }
        
        return ptr1;
    }
}

/* 
Runtime: 0 ms, faster than 100.00% of Java online submissions for Find the Duplicate Number.
Memory Usage: 42.7 MB, less than 5.09% of Java online submissions for Find the Duplicate Number.
 */

 /*
 https://www.youtube.com/watch?v=pKO9UjSeLew
 */