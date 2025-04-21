import java.util.*;

class Solution {
    public String solution(String new_id) {
        String answer = "";
        
        // 1단계
        new_id = new_id.toLowerCase();
        
        // 2, 3단계
        int len = new_id.length();
        boolean isDot = false;
        for (int i = 0; i < len; i++) {
            char c = new_id.charAt(i);
            
            if (isDot && c == '.') {
                continue;
            }
            
            if (c == '.') {
                isDot = true;
                answer += c;
            }
            
            if (c == '-' || c == '_' || Character.isDigit(c) || Character.isLowerCase(c)) {
                isDot = false;
                answer += c;
            }
        }

        // 4단계
        len = answer.length();
        String temp = "";
        for (int i = 0; i < len; i++) {
            char c = answer.charAt(i);
            
            if (c == '.') {
                temp += '.';
            } else {
                break;
            }
        }
        
        answer = answer.replaceFirst(temp, "");
        
        len = answer.length();
        for (int i = len - 1; i >= 0; i--) {
            char c = answer.charAt(i);
            
            if (c != '.') {
                answer = answer.substring(0, i + 1);
                break;
            }
        }
        
        // 5단계
        len = answer.length();
        if (len == 0) {
            answer = "a";
        }
        
        // 6
        if (len >= 16) {
            answer = answer.substring(0, 15);
        }
 
        // 4단계
        len = answer.length();
        for (int i = len - 1; i >= 0; i--) {
            char c = answer.charAt(i);
            
            if (c != '.') {
                answer = answer.substring(0, i + 1);
                break;
            }
        }

        // 7
        len = answer.length();
        if (len <= 2) {
            char c = answer.charAt(len - 1);
            while (len++ < 3) {
                answer += c;
            }
        }
        
        return answer;
    }
}