import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        List<String> list = new ArrayList<String>();    //List 사용해 ArrayList 생성
        
        for(int i = 0; i < strings.length; i++){
            list.add(strings[i].charAt(n) + strings[i]);    //n = 1 이라면 sun, bed, car -> usun, ebed, acar
        }
        
        Collections.sort(list); //Collections.sort(List<T> list) 사용
        
        for(int i = 0; i < strings.length; i++){
            answer[i] = list.get(i).substring(1);   //acar, ebed, usun -> car, bed, sun
        }
        
        return answer;
    }
}
