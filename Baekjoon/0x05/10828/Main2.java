import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

// BOJ 10828 [스택]
// 배열로 스택 구현
public class Main2 {
    static final int MAX = 10005;
    static int[] stack = new int[MAX];
    static int pos = 0;

    public static void push(int num) {
        stack[pos++] = num;
    }

    public static int pop() {
        return pos == 0 ? -1 : stack[--pos];
    }

    public static int size() {
        return pos;
    }

    public static int isEmpty() {
        return pos == 0 ? 1 : 0;
    }

    public static int peek() {
        return pos == 0 ? -1 : stack[pos-1];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; i++) {
            String[] str = br.readLine().split(" ");
            String command = str[0];

            switch (command) {
                case "push":
                    push(Integer.parseInt(str[1]));
                    break;
                case "pop":
                    bw.write(pop() + "\n");
                    break;
                case "size":
                    bw.write(size() + "\n");
                    break;
                case "empty":
                    bw.write(isEmpty() + "\n");
                    break;
                case "top":
                    bw.write(peek() + "\n");
                    break;
                default:
                    break;
            }
        }

        bw.flush();
        bw.close();
    }
}
