class Solution {
    public int countNegatives(int[][] grid) {
        int negCount = 0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                if(grid[i][j]<0){
                    negCount++;
                }
            }
        }
        return negCount;
    }
}


/*  Runtime: 1 ms, faster than 61.10% of Java online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 41.8 MB, less than 100.00% of Java online submissions for Count Negative Numbers in a Sorted Matrix.
 */