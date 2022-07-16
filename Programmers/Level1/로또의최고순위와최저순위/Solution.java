import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int matchCnt = 0;   // 맞춘 숫자 개수
        int zeroCnt = 0;    // 알아볼 수 없는 번호 개수

        List<Integer> winNums = Arrays.stream(win_nums).boxed().collect(Collectors.toList());

        for(int k : lottos) {
            if(winNums.contains(k)) matchCnt++;
            if(k == 0) zeroCnt++;
        }

        answer[0] = getRank(matchCnt + zeroCnt);
        answer[1] = getRank(matchCnt);
        
        return answer;
    }

    // 순위를 구한다 
    public int getRank(int count) {
        int rank = 6;
        switch (count) {
            case 6:
                rank = 1;
                break;
            case 5:
                rank = 2;
                break;
            case 4:
                rank = 3;
                break;
            case 3:
                rank = 4;
                break;
            case 2:
                rank = 5;
                break;
            default: break;
        }

        return rank;
    }
}
