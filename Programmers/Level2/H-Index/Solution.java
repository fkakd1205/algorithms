import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);     // 인용 횟수 배열 오름차순 정렬
        
        for(int i = 0; i < citations.length; i++) {
            int hIdx = citations.length - i;        // H-Index
            
            // 배열을 오름차순 정렬했으므로, 
            if(hIdx <= citations[i]) {
                answer = hIdx;
                break;
            }
        }
        return answer;
    }
}
