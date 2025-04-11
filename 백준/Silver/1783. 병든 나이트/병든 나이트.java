import java.io.*;
import java.util.*;

class Main {
    public static final int MAX_N = 2000000000;

    public static int n, m;
    public static int ans = 1;

    public static void main(String[] args) throws IOException {
        init();

        // N이 3이상이고 M이 6이상이라면 정답은 M - 2
        // N이 3 미만 혹은 M이 6미만이라면 최대 4
        if (n >= 3) {

            if (m >= 6) {
                ans = m - 2;
            } else {
                ans = Math.min(4, m);
            }

        } else if (n == 2) {
            ans = Math.min(4, (m - 1) / 2 + 1);
        }

        System.out.println(ans);
    }

    public static void init() throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
    }
}

