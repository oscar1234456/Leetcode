class Solution {
    public int[] decompressRLElist(int[] nums) {
        ArrayList<Integer> finalArrayList = new ArrayList<Integer>();
        for(int i=0;i<nums.length/2;i++){
            int nowAppend = nums[2*i+1];
            int nowMount = nums[2*i];
            for(int j=0;j<nowMount;j++){
                finalArrayList.add(nowAppend);
            }
        }
        int[] finalArray = new int[finalArrayList.size()];
        int count=0;
        for(Integer temp:finalArrayList){
            finalArray[count] = temp.intValue();
            count++;
        }
        return finalArray;
    }
}


/*  0ms 100%   41.4 MB, less than 100.00%
class Solution {
    public int[] decompressRLElist(int[] nums) {
        int len = 0;
        for(int i=0;i<nums.length;i+=2){
            len += nums[i];
        }

        int res[] = new int[len];
        int j=0;
        for(int i=0;i<nums.length;i+=2){
            Arrays.fill(res,j,j+nums[i],nums[i+1]);
            j = j + nums[i];
        }

        return res;
    }
}
 */