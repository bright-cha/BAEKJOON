import java.io.*;
import java.util.*;

class Main {

    public static final int MAX_CNT = 100000;
    public static int ans;
    public static Stack<Character> stack = new Stack();

    public static void main(String[] args) throws IOException {
        //  입력
        init();

        int cnt = 0;
        while (!stack.empty()) {
            char c = stack.pop();

            if (c == ')') {
                // 막대기의 끝인 경우.
                if (stack.peek() == ')') {
                    cnt++;
                } else {
                    // 레이저인 경우,
                    stack.pop();
                    ans += cnt;
                }
            } else {
                // 막대기의 시작
                cnt--;
                ans++;
            }
        }

        System.out.println(ans);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            stack.push(c);
        }
    }
}