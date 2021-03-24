import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i = 0; i < commands.length; i++){
            //Arrays.copyOfRange(복사할 배열, 시작인덱스, 끝인덱스)
            int[] array2 = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(array2);
            answer[i] = array2[commands[i][2]-1];
        }
        
        return answer;
    }
}
