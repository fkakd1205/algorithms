import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Integer[] number = new Integer[9];
        Integer[] result = new Integer[9];
        int sum = 0;
        boolean isMatched = false;

        for(int i = 0; i < 9; i++) {
            int num = scanner.nextInt();
            number[i] = num;
            result[i] = num;
            sum += num;
        }

        for(int i = 0; i < 8; i++) {
            for(int j = i+1; j < 9; j++) {
                // 모든 난쟁이들의 키 합에서 2명의 키를 뺐을 때, 100 이면 그 2명의 키를 0으로 세팅한다
                if(sum - (number[i] + number[j]) == 100) {
                    result[i] = 0;
                    result[j] = 0;
                    isMatched = true;
                    break;
                }
            }

            if(isMatched) break;
        }

        Arrays.sort(result);
        // result를 돌면서 키 값이 0이 아니라면 출력
        for(int i = 0; i < result.length; i++) {
            if(result[i] != 0) {
                System.out.println(result[i]);
            }
        }
    }
}
