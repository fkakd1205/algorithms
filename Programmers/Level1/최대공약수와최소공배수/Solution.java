class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        int a = n, b = m;
        
        // '유클리드 호제법'을 활용해 최대공약수 구하기
        while(b != 0){
            int k = a % b;
            a = b;
            b = k;
        }
        
        answer[0] = a;  // n과 m의 최대공약수
        answer[1] = n * m / a;  // n과 m의 최소공배수
        
        return answer;
    }
}
