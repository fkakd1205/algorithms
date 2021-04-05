package level1;

class Solution29 {
    public long solution(long n) {
        long answer = 0;
        
        long num = (long)Math.sqrt(n);  //제곱근 알아내기. (Math.sqrt()의 반환형은 double)
        if(num * num == n)  //위에서 알아낸 수가 제곱근이 맞다면
            answer = (long)Math.pow(num+1, 2);  //Math.pow(num+1, k). num+1의 k제곱 구하기
        else 
            answer = -1;
        return answer;
    }
}
