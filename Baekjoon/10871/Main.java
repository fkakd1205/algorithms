import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int X = scanner.nextInt();
        
        for(int i = 0; i < N; i++) {
            int number = scanner.nextInt();
            if(number < X) System.out.print(number + " ");
        }
    }
}
