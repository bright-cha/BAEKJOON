import java.io.*;
import java.util.*;

class Main {

    static final int MAX_N = 10000;
    static final int MAX_M = 100;
    static final int TEMP = 1000000007;

    static int n, m;
    static int[] dp = new int[MAX_N + 1];

    public static void main(String[] args) throws IOException {
        init();

        for (int i = m + 1; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - m]) % TEMP;
        }

        System.out.println(dp[n]);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= m; i++) {
            dp[i] = 1;
        }

        dp[m]++;
    }
}