import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";

        String[] numStr = new String[numbers.length];

        for(int i = 0; i < numbers.length; i++){
            numStr[i] = String.valueOf(numbers[i]);
        }

        // Arrays.sort(Array, Compartor)
        Arrays.sort(numStr, new Comparator<String>() {
            @Override
            public int compare(String num1, String num2) {
                return (num2 + num1).compareTo(num1 + num2);
            }
        });

        // numbers가 모두 0인 경우
        if(numStr[0].equals("0")) return "0";

        for(int i = 0; i < numStr.length; i++){
            answer += numStr[i];
        }

        return answer;
    }
}