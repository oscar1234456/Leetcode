class Solution {
    public int balancedStringSplit(String s) {
        int RLcount = 0;
        int Scount = 0;
        for(int i=0;i<s.length();i++){
            char temp = s.charAt(i);
            if(temp == 'R'){
                RLcount++;
            }else{
                RLcount--;
            }
            if(RLcount == 0){
                Scount++;
            }
        }
        return Scount;
    }
}

/*  Runtime: 0 ms, faster than 100.00% of Java online submissions for Split a String in Balanced Strings.
Memory Usage: 37.2 MB, less than 100.00% of Java online submissions for Split a String in Balanced Strings.
 */