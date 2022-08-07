import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        
        for(int i = 0; i < N; i++) {
            int[] alphabet = new int[26];
            String origin = scanner.next();
            String target = scanner.next();
            String result = "Possible";

            for(int j = 0; j < target.length(); j++) alphabet[target.charAt(j)-'a']++;
            for(int j = 0; j < origin.length(); j++) alphabet[origin.charAt(j)-'a']--;

            for(int j = 0; j < alphabet.length; j++) {
                if(alphabet[j] > 0) {
                    result = "Impossible";
                    break;
                }
            }

            System.out.println(result);
        }
    }
}
