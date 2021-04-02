import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String answer = "";
        String str[] = s.split("");
        
        Arrays.sort(str); //Arrays.sort(Array)
        Collections.reverse(Arrays.asList(str)); //Arrays.asList(Array) 배열을 List로 변환
                                                 //Collections.reverse(List<T>)
        
        for(int i = 0; i < str.length; i++)
            answer += str[i];
        
        return answer;
    }
}
