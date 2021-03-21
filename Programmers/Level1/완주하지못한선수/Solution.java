import java.util.Arrays;

//완주하지 못한 선수
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        String temp = "";
        
        //참가자와 완주자의 이름을 오름차순으로 정렬
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        //완주자 명단에 없는 참가자를 확인
        for(int i = 0; i < completion.length; i++) {
            if(!completion[i].equals(participant[i])){
                temp = participant[i];
                break;
            }
        }
        
        if(!temp.equals("")){
            answer = temp;
        }else{
            answer = participant[participant.length-1]; //완주자 명단에 없으며, 참가자 이름을 오름차순했을 때의 마지막 참가자
        }
        
        return answer;
    }
}
