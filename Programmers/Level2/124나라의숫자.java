class Solution {
    public String solution(int n) {
        String answer = "";
        String[] num = {"4", "1", "2"};
        
        while(n > 0){
            answer = num[n % 3] + answer;   // 세 숫자가 반복되므로
            n = (n - 1) / 3;  // n에서 -1해줘야 while문을 반복할때 answer에 올바른 값이 들어감.
        }
        
        return answer;
    }
}
