class Solution {
    public int[] solution(long n) {
        String str = n + "";    //n을 String형으로 변환
        int[] answer = new int[str.length()];
        int k = 0;
        
        //일의 자리 숫자부터 배열에 넣기
        while(n != 0){
            answer[k++] = (int)(n % 10);
            n /= 10;
        }
        
        return answer;
    }
}
