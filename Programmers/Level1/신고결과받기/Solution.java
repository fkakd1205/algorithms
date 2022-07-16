import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];

        HashMap<String, Integer> reportIdList = new HashMap<>();
        HashMap<String, HashSet<String>> reportDetailMap = new HashMap<>();
        
        // (id_list[0], 0), (id_list[1], 1), ...
        for(int i = 0; i < id_list.length; i++) {
            String id = id_list[i];
            reportDetailMap.put(id, new HashSet<>());
            reportIdList.put(id, i);
        }

        for(int i = 0; i < report.length; i++) {
            String[] reportDetailId = report[i].split(" ");
            String sender = reportDetailId[0];
            String receiver = reportDetailId[1];

            reportDetailMap.get(receiver).add(sender);
        }

        // k번 이상 신고받은 유저 검사
        for(String id : id_list) {
            HashSet<String> senderIdSet = reportDetailMap.get(id);
            if(senderIdSet.size() >= k) {
                for(String senderId: senderIdSet){
                    answer[reportIdList.get(senderId)]++;
                }
            }
        }
        return answer;
    }
}