import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

class Main {

    public static final int MAX_N = 100;

    public static int n;
    public static int ans = Integer.MIN_VALUE;
    public static int maxHeight = Integer.MIN_VALUE;
    public static int[][] matrix = new int[MAX_N][MAX_N];
    public static boolean[][] isChecked;
    public static Deque<int[]> stack = new ArrayDeque<>();
    public static int[][] delta = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
                maxHeight = Math.max(maxHeight, matrix[i][j]);
            }
        }

        while (--maxHeight >= 0) {
            isChecked = new boolean[n][n];
            int cnt = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (isChecked[i][j] || matrix[i][j] <= maxHeight) continue;
                    dfs(i, j, maxHeight);
                    cnt++;
                }
            }

            if (ans < cnt) {
                ans = cnt;
            }
        }

        System.out.println(ans);
    }

    public static void dfs(int x, int y, int rain) {
        stack.addLast(new int[]{x, y});
        isChecked[x][y] = true;

        while (!stack.isEmpty()) {
            int[] poll = stack.poll();
            x = poll[0];
            y = poll[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + delta[i][0];
                int ny = y + delta[i][1];

                if (canGo(nx, ny) && matrix[nx][ny] > rain && !isChecked[nx][ny]) {
                    isChecked[nx][ny] = true;
                    stack.addLast(new int[]{nx, ny});
                }
            }
        }
    }

    public static boolean canGo(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}