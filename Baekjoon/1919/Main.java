import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String firstStr = scanner.next();
        String secondStr = scanner.next();
        int[] alphabet = new int[26];
        
        for(int i = 0; i < firstStr.length(); i++) alphabet[firstStr.charAt(i) - 'a']++;
        for(int i = 0; i < secondStr.length(); i++) alphabet[secondStr.charAt(i) - 'a']--;

        int sum = 0;
        for(int i = 0; i < alphabet.length; i++) {
            sum += Math.abs(alphabet[i]);
        }

        System.out.println(sum);
    }
}