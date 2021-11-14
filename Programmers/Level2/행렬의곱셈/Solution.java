class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        // 행렬의 곱 결과 (n1 * n3) - (n1 * n2), (n2 * n3) n2가 동일해야 가능 함.
        int[][] answer = new int[arr1.length][arr2[0].length];
        
        for(int i = 0; i < arr1.length; i++){
            
            // 곱해지는 숫자
            for(int j = 0; j < arr2[0].length; j++){
                
                // 기준 숫자
                for(int k = 0; k < arr1[0].length; k++){
                    answer[i][j] += (arr1[i][k] * arr2[k][j]);
                }
            }
        }
        return answer;
    }
}
