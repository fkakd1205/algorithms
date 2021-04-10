class Solution {
    public long[] solution(long x, int n) {     // 테스트케이스 에러로 x의 타입을 int에서 long으로 변경
        long[] answer = new long[n];
        
        for(int i = 0; i < n; i++){
            answer[i] = x * (i+1);
        }
        
        return answer;
    }
}
