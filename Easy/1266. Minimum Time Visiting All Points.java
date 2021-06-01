class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int res = 0;
        
        for(int i=0;i<points.length-1;i++){
            res += Math.max(
                Math.abs(points[i+1][0]-points[i][0]),
                Math.abs(points[i+1][1]-points[i][1])
            );
        }
        
        return res;
    }
}


/*  Runtime: 0 ms, faster than 100.00% of Java online submissions for Minimum Time Visiting All Points.
Memory Usage: 39.6 MB, less than 100.00% of Java online submissions for Minimum Time Visiting All Points.
 */