import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String roomNum = scanner.next();
        int[] number = new int[10];

        for(int i = 0; i < roomNum.length(); i++) {
            int n = roomNum.charAt(i)-'0';

            if(n == 6 || n == 9){
                if(number[6] < number[9]) {
                    number[6]++;
                }else {
                    number[9]++;
                }
            }else{
                number[n]++;
            }
        }

        int max = 0;
        for(int i = 0; i < number.length; i++) {
            if(max < number[i]) {
                max = number[i];
            }
        }

        System.out.println(max);
    }
}
