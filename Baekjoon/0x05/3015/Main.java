import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public static class Pair<K, V> {
        private K height;
        private V cnt;

        public Pair(K height, V cnt) {
            this.height = height;
            this.cnt = cnt;
        }

        public K getHeight() {
            return height;
        }

        public V getCnt() {
            return cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        Stack<Pair<Integer, Integer>> stack = new Stack<>();
       
        long result = 0;
        for(int i = 0; i < N; i++) {
            int height = Integer.parseInt(br.readLine());
            int cnt = 1;

            while(!stack.isEmpty() && stack.peek().getHeight() <= height) {
                result += stack.peek().getCnt();

                // height가 동일한 사람(A, B)이 있다면 cnt를 증가
                // 다음에 stack에 쌓이는 숫자에 동일한 사람 수만큼 result를 더해줘야 한다
                if(stack.peek().getHeight() == height) {
                    cnt += stack.peek().getCnt();
                }
                stack.pop();
            }

            if(!stack.isEmpty()) {
                result++;
            }

            stack.push(new Pair<>(height, cnt));
        }

        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}
