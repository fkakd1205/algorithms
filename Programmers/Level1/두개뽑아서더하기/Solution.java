import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> list = new ArrayList<Integer>();  //List를 사용해 ArrayList 생성
        
        for(int i = 0; i < numbers.length-1; i++){
            for(int j = i+1; j < numbers.length; j++){
                int sum = numbers[i] + numbers[j];
                if(!list.contains(sum)){    //list에 같은 값이 없다면 추가
                    list.add(sum);
                }
            }
        }
        
        int[] answer = new int[list.size()];
        
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}
