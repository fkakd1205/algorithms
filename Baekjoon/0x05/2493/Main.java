import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public static class Pair<K, V> {
        private K key;
        private V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        
        Stack<Pair<Integer, Integer>> tower = new Stack<>();
        tower.push(new Pair<>(0, 100000001));
        
        String[] height = br.readLine().split(" ");
        for(int i = 0; i < N; i++) {
            int h = Integer.parseInt(height[i]);
            
            // 현재 탑의 높이보다 작은 탑은 스택에서 제거한다
            while(tower.peek().getValue() < h) {
                tower.pop();
            }

            bw.write(tower.peek().getKey() + " ");
            tower.push(new Pair<>(i+1, h));
        }

        bw.flush();
        bw.close();
    }
}
