import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[20];
    
        for(int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
    
        int sumY = 0;
        int sumM = 0;
        for(int i = 0; i < N; i++) {
            sumY += ((arr[i] / 30) + 1) * 10;
            sumM += ((arr[i] / 60) + 1) * 15;
        }
    
        if(sumY < sumM) {
            System.out.println("Y " + sumY);
        }else if(sumM < sumY) {
            System.out.println("M " + sumM);
        }else {
            System.out.println("Y M " + sumY);
        }
    }
}
