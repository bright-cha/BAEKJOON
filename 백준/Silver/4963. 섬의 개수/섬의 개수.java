import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

class Pair {
    int x;
    int y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Main {

    public static final int MAX_SIZE = 50;

    public static int w, h;
    public static int[][] matrix = new int[MAX_SIZE][MAX_SIZE];
    public static boolean[][] isChecked = new boolean[MAX_SIZE][MAX_SIZE];
    public static Deque<Pair> dq = new ArrayDeque<>();
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        // 입력(0, 0)이라면 false.
        // 입력이 true -> 풀이와 출력 진행
        while (init()) {
            isCheckedInit();

            int cnt = 0;
            for (int i = 0; i < w; i++) {
                for (int j = 0; j < h; j++) {
                    if (matrix[i][j] == 1 && !isChecked[i][j]) {
                        // 9방향으로 dfs 진행 및 체크
                        dfs(i, j);
                        cnt++;
                    }
                }
            }
            // 갯수 출력.
            System.out.println(cnt);
        }
    }

    public static void dfs(int x, int y) {
        dq.add(new Pair(x, y));
        isChecked[x][y] = true;

        while (!dq.isEmpty()) {
            Pair pair = dq.poll();

            x = pair.x;
            y = pair.y;

            for (int i = -1; i < 2; i++) {
                for (int j = -1; j < 2; j++) {
                    int nx = x + i;
                    int ny = y + j;

                    if (canGo(nx, ny)) {
                        dq.addLast(new Pair(nx, ny));
                        isChecked[nx][ny] = true;
                    }
                }
            }
        }
    }

    public static boolean canGo(int x, int y) {
        return 0 <= x && x < w && 0 <= y && y < h && !isChecked[x][y] && matrix[x][y] == 1;
    }

    public static void isCheckedInit() {
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                isChecked[i][j] = false;
            }
        }
    }

    public static boolean init() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());

        if (w == 0 && h == 0) return false;

        for (int i = 0; i < w; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < h; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        return true;
    }
}