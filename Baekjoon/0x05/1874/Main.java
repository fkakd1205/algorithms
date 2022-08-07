import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        int[] data = new int[N];

        for(int i = 0; i < N; i++) {
            data[i] = Integer.parseInt(br.readLine());
        }

        int idx = 0;
        for(int i = 1; i <= N; i++) {
            stack.push(i);
            sb.append("+").append("\n");

            while(true) {
                // 스택의 맨 위의 데이터와 현재 idx가 가리키는 데이터와 비교
                if(!stack.isEmpty() && (stack.peek() == data[idx])) {
                    stack.pop();
                    sb.append("-").append("\n");
                    idx++;
                }else {
                    break;
                }
            }
        }

        if(stack.isEmpty()) {
            bw.write(sb.toString());
        }else {
            System.out.println("NO");
        }

        bw.flush();
        bw.close();
    }
}
