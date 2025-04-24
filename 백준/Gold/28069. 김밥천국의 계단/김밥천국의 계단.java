import java.io.*;
import java.util.*;

class Node {
    int cur;
    int cnt;

    public Node(int cur, int cnt) {
        this.cur = cur;
        this.cnt = cnt;
    }
}

class Main {

    public static int n, k;
    public static boolean isPossible;
    public static int[] dp;


    public static void main(String[] args) throws  IOException {
        init();

        bfs();

        if (isPossible) {
            System.out.println("minigimbob");
        } else {
            System.out.println("water");
        }
    }

    public static void bfs() {
        Arrays.fill(dp, 1000001);
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 1; i < n; i++) {
            if (i + 1 <= n) {
                dp[i + 1] = Math.min(dp[i + 1], dp[i] + 1);
            }
            if (i + i / 2 <= n) {
                dp[i + i / 2] = Math.min(dp[i + i / 2], dp[i] + 1);
            }
        }

        if (dp[n] <= k) {
            isPossible = true;
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        dp = new int[n + 1];
    }
}