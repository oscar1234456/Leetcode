class Solution {
    public int coinChange(int[] coins, int amount) {
        int coin[] = new int[coins.length+1];
        coin[0] = 0;
         for(int j=1;j<coin.length;j++){
                coin[j] =coins[j-1];
            }
            int dp[][] = new int[coin.length][amount+1]; 
        
            for(int j=1;j<=amount;j++){
                dp[0][j] = Integer.MAX_VALUE-1;
            }
            for(int j=0;j<coin.length;j++){
                dp[j][0] = 0;
            }  
            for(int k=1;k<coin.length;k++){
                for(int j=1;j<coin[k];j++){
                        if(j>amount){break;}
                        dp[k][j]=dp[k-1][j];
                }
                for(int j=coin[k];j<=amount;j++){
                    dp[k][j] = Math.min(dp[k-1][j],1+dp[k][j-coin[k]]);
                }
            }     
            if(dp[coin.length-1][amount] == (Integer.MAX_VALUE-1)){
               return -1;
            }else{
                return dp[coin.length-1][amount];
            }   
          
    }
}

/* Runtime: 18 ms, faster than 33.53% of Java online submissions for Coin Change.
Memory Usage: 41.5 MB, less than 5.33% of Java online submissions for Coin Change.
 */