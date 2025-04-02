import java.util.*;

class Solution {
    
    // 각 좌표의 최소 최대를 담을 배열
    public static int[] xArr = new int[2];
    public static int[] yArr = new int[2];
    
    public int[] solution(String[] wallpaper) {
        
        xArr[0] = Integer.MAX_VALUE;
        yArr[0] = Integer.MAX_VALUE;
        
        
        for (int i = 0; i < wallpaper.length; i++) {
            for (int j = 0; j < wallpaper[0].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    xArr[0] = Math.min(xArr[0], i);
                    xArr[1] = Math.max(xArr[1], i);
                    yArr[0] = Math.min(yArr[0], j);
                    yArr[1] = Math.max(yArr[1], j);
                }
            }
        }
        
        
        int[] answer = {xArr[0], yArr[0], xArr[1] + 1, yArr[1] + 1};
        return answer;
    }
}