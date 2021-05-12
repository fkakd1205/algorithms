class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for(int i = 0; i < prices.length; i++){
            for(int j = i+1; j < prices.length; j++){
                if(prices[j] < prices[i]) {    // 주식가격이 떨어진다면
                	answer[i] = j-i;    // 떨어진 인덱스 값 - 현재 인덱스 값
                	break;
                }
            }
            if(answer[i] == 0) answer[i] = prices.length-1-i;   // 주식가격이 떨어지지 않았다면 
        }
        return answer;
    }
}
