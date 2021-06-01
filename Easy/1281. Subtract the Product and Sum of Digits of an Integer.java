class Solution {
    public int subtractProductAndSum(int n) {
        boolean keep = true;
        int pd = 1;
        int sd = 0;
        while(keep){
            int nextDigit = n%10;
            pd*=nextDigit;
            sd+=nextDigit;
            if((n/=10) == 0){
                keep = false;
            }
        }

        return pd - sd;

    }
}


/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 36.2 MB, less than 100.00% of Java online submissions for Subtract the Product and Sum of Digits of an Integer.
 */