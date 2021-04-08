class Solution {
    public int solution(int num) {
        int answer = 0;
        int cnt = 0;
        
        while(num != 1 && cnt != 500){
            if(num % 2 == 0)    // 짝수 일때
                num /= 2;
            else if(num % 2 == 1)   // 홀수 일때
                num = (num * 3) + 1;
            
            cnt++;
        }
        answer = cnt;
        
        if(cnt == 500) answer = -1; // 작업을 500번 반복해도 1이 되지 않았을 때
        
        return answer;
    }
}
