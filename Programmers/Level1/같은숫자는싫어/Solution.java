import java.util.List;
import java.util.ArrayList;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        List<Integer> num = new ArrayList<Integer>();   //List를 사용해 ArrayList 생성
        
        num.add(arr[0]);    //첫번째 요소를 먼저 넣어준다.
        for(int i = 1; i < arr.length; i++){    //첫번째 요소를 미리 넣고 for문을 실행 -> 마지막 요소까지 num에 넣을 수 있다.
            if(arr[i] != arr[i-1])
                num.add(arr[i]);
        }
        
        answer = new int[num.size()];
        
        for(int i = 0; i < num.size(); i++)
            answer[i] = num.get(i);

        return answer;
    }
}
