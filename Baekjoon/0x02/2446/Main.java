import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int startIdx = 0;   // 별 시작 인덱스
        int endIdx = (2 * N) - 2;   // 별 끝 인덱스

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < startIdx; j++) System.out.print(" ");
            for(int j = startIdx; j <= endIdx; j++) System.out.print("*");

            startIdx++;
            endIdx--;
            System.out.print("\n");
        }

        int temp = startIdx;
        startIdx = endIdx;
        endIdx = temp;

        for(int i = 0; i < (N-1); i++) {
            for(int j = 0; j < startIdx; j++) System.out.print(" ");
            for(int j = startIdx; j <= endIdx; j++) System.out.print("*");

            startIdx--;
            endIdx++;
            System.out.print("\n");
        }

    }
}
