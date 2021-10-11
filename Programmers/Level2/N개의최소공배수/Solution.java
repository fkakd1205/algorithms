class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int exLcm = arr[0];

        // 차례로 두 수의 최소공배수를 구한다
        for(int i = 1; i < arr.length; i++) {
            exLcm = lcm(exLcm, arr[i]);
        }
        answer = exLcm;
        return answer;
    }

    // '유클리드 호제법'을 사용해서 최대공약수, 최소공배수 추출
    public int lcm(int a, int b) {
        int n = a;
        int m = b;
        int gcd = 1;

        while(b != 0) {
            int k = a % b;
            a = b;
            b = k;
        }

        gcd = a;        // 최대공약수
        return (n * m / gcd);       // 최소공배수
    }
}
