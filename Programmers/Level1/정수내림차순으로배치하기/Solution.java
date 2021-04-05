import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String str = n + "";    //n을 String형으로 변환변환.
        String num[] = str.split("");   //한글자씩 배열에 넣기.
        
        Arrays.sort(num);   //Arrays.sort(Array)
        Collections.reverse(Arrays.asList(num));    //Arrays.asList(Array), Collections.reverse(List)

        answer += Long.parseLong(String.join("", num)); //String.join(String, String[]) 구분 기호로 배열의 요소들을 연결.
            
        return answer;
    }
}
