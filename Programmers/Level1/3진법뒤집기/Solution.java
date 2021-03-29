import java.util.List;
import java.util.ArrayList;
import java.lang.Math;

class Solution {
    public int solution(int n) {
        int answer = 0;
        List<Integer> num = new ArrayList<Integer>();   //List를 사용해서 ArrayList 생성
        
        //3진법으로 변환
        while(true){
            if(n==0) break;
            
            num.add(n%3);
            n /= 3;
        }
        
        //3진법을 뒤집어서 10진법으로 변환
        for(int i = 0; i < num.size(); i++){
            answer += (Math.pow(3, num.size()-1-i)) * num.get(i);
        }
        
        return answer;
    }
}
