import java.util.Scanner;

// 10808
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();
        int[] alphabet = new int[26];

        for(int i = 0; i < word.length(); i++) {
            alphabet[word.charAt(i) - 'a']++;
        }

        for(int i = 0; i < num.length; i++) {
            System.out.print(alphabet[i] + " ");
        }
    }
}
