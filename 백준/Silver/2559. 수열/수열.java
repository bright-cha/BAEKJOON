import java.util.Scanner;

class Main {

    public static final int MAX_N = 100000;

    public static int n, k;
    public static int ans = Integer.MIN_VALUE;
    public static int[] arr = new int[MAX_N];

   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);

       n = sc.nextInt();
       k = sc.nextInt();

       for (int i = 0; i < n; i++) {
           arr[i] = sc.nextInt();
       }

       int num = 0;
       for (int i = 0; i < k; i++) {
           num += arr[i];
       }
       ans = Math.max(ans, num);

       for (int i = k; i < n; i++) {
           num -= arr[i - k];
           num += arr[i];
           ans = Math.max(ans, num);
       }

       System.out.println(ans);
   }
}