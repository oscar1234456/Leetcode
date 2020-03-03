class Solution {
    public String toLowerCase(String str) {
        char[] res = new char[str.length()];
        for(int i=0;i<str.length();i++){
            char temp = str.charAt(i);
            int unico = (int)temp;
           if(unico >= 65 && unico <= 90){
                res[i] = (char)(unico+32) ;
            }else{
                res[i] = temp;
            }
        }
        
        return String.valueOf(res);
    }
}


/*  Runtime: 0 ms, faster than 100.00% of Java online submissions for To Lower Case.
Memory Usage: 37.6 MB, less than 6.49% of Java online submissions for To Lower Case.
 */