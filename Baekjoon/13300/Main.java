import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        int totalRoom = 0;
        
        int[][] grade = new int[6][2];

        for(int i = 0; i < N; i++) {
            int s = scanner.nextInt();
            int g = scanner.nextInt();
            // 1학년 -> 0, 2학년 -> 1, ...
            grade[g-1][s]++;
        }

        for(int i = 0; i < grade.length; i++) {
            for(int j = 0; j < grade[i].length; j++) {
                int num = grade[i][j];
                totalRoom += num / K;
                // 나머지가 존재한다면 +1
                if((num % K) > 0) {
                    totalRoom++;
                }
            }
        }

        System.out.println(totalRoom);
    }
}
