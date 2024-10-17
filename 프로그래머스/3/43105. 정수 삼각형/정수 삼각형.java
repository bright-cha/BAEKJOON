import java.io.*;
import java.util.*;

class Solution {
    public static final int MAX_HEIGHT = 500;
    public static final int MAX_VALUE = 9999;
    // 높이와 위치에 따른 최댓값을 구하기 위한 DP
    public static int[][] dp = new int[MAX_HEIGHT][MAX_HEIGHT];
    
    public int solution(int[][] triangle) {
        int answer = 0;
        int maxHeight = triangle.length;
        dp[0][0] = triangle[0][0];
        
        for (int i = 1; i < maxHeight; i++) {
            dp[i][0] = dp[i - 1][0] + triangle[i][0];
            for (int j = 1; j < i; j++) {
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j] + triangle[i][j]);
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - 1] + triangle[i][j]);
                
            }
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i];
        }
        
        for (int i = 0; i < maxHeight; i++) {
            answer = Math.max(answer, dp[maxHeight - 1][i]);
        }
        
        return answer;
    }
}