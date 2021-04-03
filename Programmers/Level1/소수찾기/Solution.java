class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean[] check = new boolean[n+1]; //n도 소수인지 판별해야 함
        
        //'에라토스테네스의 체'를 활용해 소수 판별
        for(int i = 2; i <= n; i++){
            if(check[i] == false)   //합성수로 지정되지 않았으며, 처음 나오는 값을 소수로 지정
                answer++;
            for(int j = i; j <= n; j += i){  //i를 곱하여 나올 수 있는 값을 미리 합성수로 지정
                if(check[j] == false)
                    check[j] = true;
            }
        }
        return answer;
    }
}
