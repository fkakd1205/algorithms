import java.util.LinkedList;
import java.util.Scanner;

// BOJ 1158 [요세푸스]
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] str = sc.nextLine().split(" ");

        int N = Integer.parseInt(str[0]);
        int K = Integer.parseInt(str[1]);

        LinkedList<Integer> list = new LinkedList<>();
        // 1 ~ N 까지의 숫자를 넣는다
        for (int i = 1; i <= N; i++) {
            list.add(i);
        }

        int rmIdx = 0;
        System.out.print("<");
        while (list.size() != 0) {
            // 요세푸스 순열 구하는 공식
            rmIdx = (rmIdx + (K-1)) % list.size();
            System.out.print(list.remove(rmIdx));

            if(list.size() > 0) {
                System.out.print(", ");
            }
        }
        System.out.print(">");
    }
}
