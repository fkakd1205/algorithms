import java.util.Arrays;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;

        // 오름차순 정렬
        Arrays.sort(A);
        Arrays.sort(B);

        // A배열에 작은 수부터 B배열에 큰 수를 곱하여 더한다
        for(int i = 0; i < A.length; i++) {
            answer += (A[i] * B[(B.length-1) - i]);
        }

        return answer;
    }
}
