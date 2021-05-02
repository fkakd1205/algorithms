import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] unClear = new int[N+2];   // 현재 멈춰있는 스테이지의 인원
        double[] unClearPer = new double[N+1];    // 각 단계의 실패율
        int clear = stages.length;  // 해당 단계를 이미 진행했거나 머무르는 인원
        List<Double> fail = new ArrayList<Double>();    // 실패율을 내림차순 하기 위해
        
        // 각 단계마다 멈춰있는 인원을 구한다.
        for(int k : stages){
            unClear[k]++;
        }
        
        for(int i = 1; i <= N; i++){
            if(clear > 0)
                unClearPer[i] = (float)unClear[i] / clear;   // 실패율 계산
            else
                unClearPer[i] = 0;
            
            clear -= unClear[i];    // 다음 단계에 아직 도달하지 못한 인원을 빼준다.
            fail.add(unClearPer[i]);
        }
        
        Collections.sort(fail, Collections.reverseOrder()); // 내림차순 정렬
        
        // 내림차순 된 fail과 실패율 unClearPer의 요소를 비교해서 같으면
        // 스테이지번호를 실패율이 높은 순으로 answer배열에 넣는다.
        for(int i = 0; i < fail.size(); i++){
            for(int j = 1; j < unClearPer.length; j++){
                if(fail.get(i) == unClearPer[j]){
                    answer[i] = j;
                    unClearPer[j] = -1;
                    break;
                }
            }
        }
        
        return answer;
    }
}
