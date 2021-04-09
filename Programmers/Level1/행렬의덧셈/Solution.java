class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];  // arr1과 arr2의 행과 열 크기 동일하므로, 둘 중 하나의 행과 열 크기로 answer크기 지정. (arr.length - 행 크기, arr[0].length - 열 크기)
        
        for(int i = 0; i < arr1.length; i++){
            for(int j = 0; j < arr1[0].length; j++){
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        
        return answer;
    }
}
