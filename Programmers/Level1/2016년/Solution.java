class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int day = 0;
        
        //2016년의 1월 1일 금요일, week의 첫번째 요소를 FRI로 설정
        String week[] = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
        //2016년 각 달의 마지막 날
        int month[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        for(int i = 0;i < a-1; i++){
            day += month[i];
        }
        
        day += b-1; //ex) 1월 1일이 금요일이 되려면, -1을 해줘야 week의 FRI값을 가질 수 있다.
        answer = week[day%7 - 1];
        
        return answer;
    }
}
