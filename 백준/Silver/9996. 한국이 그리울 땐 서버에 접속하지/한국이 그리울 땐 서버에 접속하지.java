import java.io.*;
import java.util.*;

class Main {

    public static final int MAX_N =  100;

    public static int n;
    public static String pattern = "", startPattern = "", endPattern = "";
    public static int startLength, endLength;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        init();

        while (n-- > 0) {
            boolean matchStart = false;
            boolean endStart = false;
            
            String input = br.readLine();
            int inputLength = input.length();

            if (inputLength >= startLength + endLength) {
                matchStart = input.substring(0, startLength).equals(startPattern);
                endStart = input.substring(inputLength - endLength).equals(endPattern);
            }
            
            if (matchStart && endStart) {
                System.out.println("DA");
            } else {
                System.out.println("NE");
            }
        }
    }

    public static void init() throws IOException {
        n = Integer.parseInt(br.readLine());
        pattern = br.readLine();

        boolean isStartPattern = true;
        for (int i = 0; i < pattern.length(); i++) {
            if (pattern.charAt(i) == '*') {
                isStartPattern = false;
                continue;
            }

            if (isStartPattern) {
                startPattern += pattern.charAt(i);
            } else {
                endPattern += pattern.charAt(i);
            }
        }

        startLength = startPattern.length();
        endLength = endPattern.length();
    }
}