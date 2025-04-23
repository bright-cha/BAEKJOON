import java.io.*;
import java.util.*;

class Main {

    public static final int MAX_N = 100000;
    public static final int MAX_M = 100;

    public static int n, m, a, b, ans;
    public static boolean[] closed;
    public static int[] memo;

    public static void main(String[] args) throws IOException {
        init();

        for (int i = 0; i <= n; i++) {
            if (closed[i] || memo[i] == Integer.MAX_VALUE) continue;

            if (i + a <= n) {
                memo[i + a] = Math.min(memo[i] + 1, memo[i + a]);
            }

            if (i + b <= n) {
                memo[i + b] = Math.min(memo[i] + 1, memo[i + b]);
            }

        }

        if (memo[n] == Integer.MAX_VALUE) {
            System.out.println(-1);
        }
        else {
            System.out.println(memo[n]);
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        closed = new boolean[n + 1];
        memo = new int[n + 1];
        Arrays.fill(memo, Integer.MAX_VALUE);
        memo[0] = 0;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            for (int j = l; j <= r; j++) {
                closed[j] = true;
            }
        }
    }
}