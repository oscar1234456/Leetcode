// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        int quest[] = new int[10];
        int i = 10;
        while(i>0){
            quest[i-1] = i;
            i--;
        }
        System.out.println(binarySearch(quest,0,9,3));

        for(int temp:quest){
            System.out.println(temp);
        }
    }

    public static int binarySearch(int[] arr, int start, int end, int hkey){
        if (start > end)
            return -1;

        int mid = start + (end - start)/2;    //防止溢位
        if (arr[mid] > hkey)
            return binarySearch(arr, start, mid - 1, hkey);
        if (arr[mid] < hkey)
            return binarySearch(arr, mid + 1, end, hkey);
        return mid;

    }
}