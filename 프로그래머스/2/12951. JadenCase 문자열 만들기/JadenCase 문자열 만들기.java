import java.util.*;
import java.io.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        int len = s.length();
        boolean isFirst = true;
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            
            if (c == ' ') {
                isFirst = true;
            } else if (isFirst) {
                c = Character.toUpperCase(c);
                isFirst = false;
            } else {
                c = Character.toLowerCase(c);
            }
            
            answer += c;
        }
        
        return answer;
    }
}