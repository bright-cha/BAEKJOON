import java.io.*;
import java.util.*;

class Room {
    int e;
    long v;

    public Room(int e, long v) {
        this.e = e;
        this.v = v;
    }
}

class Main {

    static final int MAX_N = 5000;
    static final int MAX_C = 1000000000;

    static int n;
    static ArrayList<Room>[] list;
    static long[] memo;

    public static void main(String[] args) throws IOException {
        init();

        bfs();

        long ans = 0;
        for (int i = 1; i < n; i++) {
            ans = Math.max(ans, memo[i]);
        }

        System.out.println(ans);
    }

    public static void bfs() {
        Deque<Room> dq = new ArrayDeque<>();
        dq.addLast(new Room(0, 0));
        while (!dq.isEmpty()) {
            Room r = dq.poll();
            int e = r.e;
            long v = r.v;

            for (Room room : list[e]) {
                if (0 == memo[room.e]) {
                    memo[room.e] = v + room.v;
                    dq.addLast(new Room(room.e, room.v + v));
                }
            }
        }
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        memo = new long[n];
        list = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());

            list[a].add(new Room(b, c));
            list[b].add(new Room(a, c));
        }
    }
}