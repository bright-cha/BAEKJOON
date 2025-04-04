import java.util.Scanner;

class Main {

    public static final int MAX_N = 100000;

    public static int n, k;
    public static int ans = Integer.MIN_VALUE;
    public static int[] arr = new int[MAX_N];
    public static int[] memo;

   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);

       n = sc.nextInt();
       k = sc.nextInt();

       memo = new int[n - k + 1];

       for (int i = 0; i < n; i++) {
           arr[i] = sc.nextInt();
       }

       for (int i = 0; i < n - k + 1; i++) {
           for (int j = 0; j < k; j++) {
               memo[i] += arr[i + j];
           }

           ans = Math.max(ans, memo[i]);
       }

       System.out.println(ans);
   }
}