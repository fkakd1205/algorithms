class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int a = x, sum = 0;
        
        while(a != 0){
            sum += a % 10;  // 현재 a의 일의 자릿수를 더해준다.
            a /= 10;    // a를 10으로 나눠 일의 자릿수를 구할 수 있도록 한다.
        }
        
        if(x % sum != 0) answer = false;
        
        return answer;
    }
}
