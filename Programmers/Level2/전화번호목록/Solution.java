import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Map<String, Integer> map = new HashMap<>();
        
        for(int i = 0 ; i < phone_book.length; i++)
            map.put(phone_book[i], i);

        for(int i = 0 ; i < phone_book.length; i++){
            for(int j = 1 ; j < phone_book[i].length(); j++){
                // map에 번호의 접두어가 존재한다면
                if(map.containsKey(phone_book[i].substring(0, j)))
                    return false;    
            }
        }
        return answer;
    }
}
