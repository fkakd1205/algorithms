import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static final int MAX = 10000;
    static int[] queue = new int[MAX];
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
        return rear - head;
    }

    public static int empty() {
        return (size() == 0) ? 1 : 0;
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

            if(input[0].equals("push")) {
                push(Integer.parseInt(input[1]));
            }else if(input[0].equals("pop")) {
                bw.write(front() + "\n");
                pop();
            }else if(input[0].equals("size")) {
                bw.write(size() + "\n");
            }else if(input[0].equals("empty")) {
                bw.write(empty() + "\n");
            }else if(input[0].equals("front")) {
                bw.write(front() + "\n");
            }else if(input[0].equals("back")){
                bw.write(back() + "\n");
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
