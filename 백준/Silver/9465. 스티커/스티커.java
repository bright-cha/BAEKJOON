import java.io.*;
import java.util.*;

class Main {

    public static final int MAX_N = 100000;
    public static int t, n;
    public static int[][] points = new int[2][MAX_N + 1];
    public static int[][] dp;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            // 점수 입력
            init();

            for (int i = 2; i <= n; i++) {
                dp[0][i] = Math.max(dp[0][i], dp[1][i - 1] + points[0][i]);
                dp[0][i] = Math.max(dp[0][i], dp[0][i - 2] + points[0][i]);
                dp[0][i] = Math.max(dp[0][i], dp[1][i - 2] + points[0][i]);
                dp[1][i] = Math.max(dp[1][i], dp[0][i - 1] + points[1][i]);
                dp[1][i] = Math.max(dp[1][i], dp[0][i - 2] + points[1][i]);
                dp[1][i] = Math.max(dp[1][i], dp[1][i - 2] + points[1][i]);
            }

            // 최대 점수 출력
            System.out.println(Math.max(dp[0][n], dp[1][n]));
        }
    }

    private static void init() throws IOException {
        n = Integer.parseInt(br.readLine());
        dp = new int[2][n + 1];

        for (int i = 0; i < 2; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                points[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = points[i][j];
            }
        }
    }
}