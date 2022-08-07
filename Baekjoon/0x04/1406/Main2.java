import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

// BOJ 1406 [에디터]
// 스택 사용
public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        int n = Integer.parseInt(br.readLine());

        Stack<Character> leftStack = new Stack<>();
        Stack<Character> rightStack = new Stack<>();

        for(int i = 0; i < str.length(); i++) {
            leftStack.push(str.charAt(i));
        }

        for(int i = 0; i < n; i++) {
            String command = br.readLine();
            char c = command.charAt(0);

            if(c == 'L') {
                if(!leftStack.isEmpty()) {
                    rightStack.push(leftStack.pop());
                }
            }else if(c == 'D') {
                if(!rightStack.isEmpty()) {
                    leftStack.push(rightStack.pop());
                }
            }else if(c == 'B') {
                if(!leftStack.isEmpty()) {
                    leftStack.pop();
                }
            }else if(c == 'P') {
                leftStack.push(command.charAt(2));
            }
        }

        while(!leftStack.isEmpty()) {
            rightStack.push(leftStack.pop());
        }

        while(!rightStack.isEmpty()) {
            bw.write(rightStack.pop());
        }

        bw.flush();
        bw.close();
    }
}
