class Solution {
    public int maximum69Number (int num) {
        String nums = Integer.toString(num);
        char res[] = new char[nums.length()]  ; 
        boolean isChange = false;
        for(int i=0;i<nums.length();i++){
            if(isChange == false && nums.charAt(i) == '6' ){
                res[i] = '9';
                isChange = true;
            }else{
                res[i] = nums.charAt(i);
            }
        }
        
        return Integer.parseInt(String.valueOf(res));
    }
}

/* Runtime: 0 ms, faster than 100.00% of Java online submissions for Maximum 69 Number.
Memory Usage: 36.4 MB, less than 100.00% of Java online submissions for Maximum 69 Number.
 */