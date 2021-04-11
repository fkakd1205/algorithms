import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        
        Arrays.sort(d); // 오름차순으로 정렬
        
        for(int i = 0; i < d.length; i++){
            budget -= d[i];
            
            if(budget == 0){    // 예산과 딱맞게 구매했을 때
                answer = i+1;
                break;
            }else if(budget < 0){   // 예산이 남게 구매했을 때
                answer = i;
                break;
            }
        }
        
        // 모든 물품을 구매 후 예산이 남았다면
        if(budget > 0){
            answer = d.length;
        }
        
        return answer;
    }
}
