import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    public static final int MAX_N = 100000;

    public static int n, k;
    public static int ans = Integer.MIN_VALUE;
    public static int[] arr = new int[MAX_N];

   public static void main(String[] args) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer st = new StringTokenizer(br.readLine());

       n = Integer.parseInt(st.nextToken());
       k = Integer.parseInt(st.nextToken());

       st = new StringTokenizer(br.readLine());
       for (int i = 0; i < n; i++) {
           arr[i] = Integer.parseInt(st.nextToken());
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