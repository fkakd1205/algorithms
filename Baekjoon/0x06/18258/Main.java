import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static final int MAX = 2000000;
    static final int[] queue = new int[MAX];
    static int head = 0;
    static int rear = 0;

    public static void push(int value) {
        queue[rear++] = value;
    }

    public static void pop() {
        if(head != rear) {
            head++;
        }
    }

    public static int size() {
        return rear-head;
    }

    public static int empty() {
        return (head == rear) ? 1 : 0;
    }

    public static int front() {
        return (head == rear) ? -1 : queue[head];
    }

    public static int back() {
        return (head == rear) ? -1 : queue[rear-1];
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());

        while(N-- > 0) {
            String[] input = br.readLine().split(" ");

            switch(input[0]) {
                case "push": 
                    int value = Integer.parseInt(input[1]);
                    push(value);
                    break;
                case "pop":
                    bw.write(front() + "\n");
                    pop();
                    break;
                case "size":
                    bw.write(size() + "\n");
                    break;
                case "empty":
                    bw.write(empty() + "\n");
                    break;
                case "front":
                    bw.write(front() + "\n");
                    break;
                case "back":
                    bw.write(back() + "\n");
                    break;
                default: break;
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
